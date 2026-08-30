#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
SOC report export - writes .docx / .xlsx / .pptx deliverables via the officecli resident pipe.
"""
from __future__ import annotations
import json, os
from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import mcp
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.subprocess import _validate_path

try:
    import officecli
    OFFICECLI_AVAILABLE = True
except ImportError:
    OFFICECLI_AVAILABLE = False


class DocxSection(BaseModel):
    heading: str = Field(..., max_length=200)
    paragraphs: list[str] = Field(default_factory=list, max_length=50)
    bullets: list[str] = Field(default_factory=list, max_length=50)


class XlsxSheet(BaseModel):
    name: str = Field(..., max_length=40)
    headers: list[str] = Field(..., max_length=50)
    rows: list[list[str]] = Field(..., max_length=5000)


class PptxSlide(BaseModel):
    title: str = Field(..., max_length=200)
    bullets: list[str] = Field(default_factory=list, max_length=20)
    notes: str = Field(default="", max_length=1000)


class ReportExportInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    format: Literal["docx", "xlsx", "pptx"] = Field(..., description="Output format.")
    path: str = Field(..., max_length=500, description="Absolute output file path (.docx/.xlsx/.pptx).")
    docx_sections: list[DocxSection] = Field(default_factory=list,
        description="For format='docx': narrative sections with headings, paragraphs, bullets.")
    xlsx_sheets: list[XlsxSheet] = Field(default_factory=list,
        description="For format='xlsx': sheets with headers and row data.")
    pptx_slides: list[PptxSlide] = Field(default_factory=list,
        description="For format='pptx': slides with title, bullets, speaker notes.")
    title: str = Field(default="SOC Report", max_length=200,
        description="Report title (used in docx heading / pptx first slide).")


def _excel_col(idx: int) -> str:
    """Excel column letter for 0-based index: 0->A, 25->Z, 26->AA, 51->AZ, 52->BA."""
    col = ""
    n = idx + 1
    while n:
        n, rem = divmod(n - 1, 26)
        col = chr(65 + rem) + col
    return col


@mcp.tool(name="blueteam_export_report",
          annotations={"readOnlyHint": False, "destructiveHint": True,
                       "idempotentHint": True, "openWorldHint": False})
async def blueteam_export_report(params: ReportExportInput) -> str:
    """Generate a SOC report deliverable (.docx / .xlsx / .pptx) via officecli.

    Converts structured findings from MCP analysis tools into an Office document
    written through the officecli named-pipe resident. Supports:
      - docx: narrative incident report (sections -> headings/paragraphs/bullets)
      - xlsx: IOC / blocklist / compliance tables (sheets -> headers + rows)
      - pptx: executive briefing (slides -> title + bullets + speaker notes)

    **Requires**: officecli binary. If `officecli-sdk` is installed but the CLI is
    missing, it is auto-provisioned on first use (see MAESTRO supply-chain note -
    pre-stage the binary in production).

    **Worked Examples**

    1. *DOCX incident report*:
       ``blueteam_export_report(format="docx", path="/var/reports/incident.docx",
         title="Zimbra Brute Force", docx_sections=[{"heading":"Summary","paragraphs":["IP 117.247.110.24 ..."],"bullets":[]}])``

    2. *XLSX blocklist table*:
       ``blueteam_export_report(format="xlsx", path="/var/reports/blocklist.xlsx",
         xlsx_sheets=[{"name":"Blocked","headers":["IP","Score"],"rows":[["1.2.3.4","80"]]}])``

    3. *PPTX executive briefing*:
       ``blueteam_export_report(format="pptx", path="/var/reports/briefing.pptx",
         pptx_slides=[{"title":"Top Threats","bullets":["Brute force: 1,200 events"],"notes":"Escalate"}]])``
    """
    _audit_log("blueteam_export_report", {"format": params.format, "path": params.path})
    if not OFFICECLI_AVAILABLE:
        return json.dumps({"error": "officecli-sdk not installed. Run: pip install officecli-sdk"}, indent=2)

    # Write scope: BLUETEAM_EXPORT_DIR only (matches capture_traffic pattern)
    # NOT the shared read allowlist, which includes /etc (would allow --force overwrites)
    export_dir = os.environ.get("BLUETEAM_EXPORT_DIR", "/var/log/blue-team-mcp/exports")
    path = os.path.abspath(params.path)
    ok, err = _validate_path(path, [export_dir])
    if not ok:
        return json.dumps({"error": f"Path not allowed: {err}", "allowed": [export_dir]}, indent=2)
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None

    try:
        with officecli.create(path, "--force") as doc:
            if params.format == "docx":
                if params.docx_sections:
                    for sec in params.docx_sections:
                        doc.send({"command": "add", "path": "/body",
                                  "type": "paragraph",
                                  "props": {"text": sec.heading, "bold": "true",
                                             "style": "Heading1", "size": "16pt",
                                             "spaceAfter": "8pt"}})
                        for p in sec.paragraphs:
                            doc.send({"command": "add", "path": "/body",
                                      "type": "paragraph", "props": {"text": p}})
                        for b in sec.bullets:
                            doc.send({"command": "add", "path": "/body",
                                      "type": "paragraph",
                                      "props": {"text": f"• {b}"}})
                else:
                    doc.send({"command": "add", "path": "/body",
                              "type": "paragraph", "props": {"text": params.title, "bold": "true"}})

            elif params.format == "xlsx":
                if params.xlsx_sheets:
                    for sheet in params.xlsx_sheets:
                        sheet_name = sheet.name[:31]
                        for ci, h in enumerate(sheet.headers):
                            cell = f"/{sheet_name}/{_excel_col(ci)}1"
                            doc.send({"command": "set", "path": cell,
                                      "props": {"text": h, "bold": "true"}})
                        for ri, row in enumerate(sheet.rows, start=2):
                            for ci, val in enumerate(row):
                                cell = f"/{sheet_name}/{_excel_col(ci)}{ri}"
                                doc.send({"command": "set", "path": cell,
                                          "props": {"text": str(val)}})

            elif params.format == "pptx":
                if params.pptx_slides:
                    for i, slide in enumerate(params.pptx_slides, start=1):
                        doc.send({"command": "add", "path": "/",
                                  "type": "slide",
                                  "props": {"layout": "blank", "background": "FFFFFF"}})
                        # Title at top (explicit geometry required on blank layout)
                        doc.send({"command": "add", "path": f"/slide[{i}]",
                                  "type": "shape",
                                  "props": {"text": slide.title, "bold": "true",
                                             "x": "1.5cm", "y": "1.2cm",
                                             "width": "30cm", "height": "2cm"}})
                        # Bullets stacked below title, each on its own line
                        for bi, b in enumerate(slide.bullets):
                            doc.send({"command": "add", "path": f"/slide[{i}]",
                                      "type": "shape",
                                      "props": {"text": b,
                                                 "x": "1.5cm", "y": f"{3.8 + bi * 1.1}cm",
                                                 "width": "30cm", "height": "1cm"}})
                        if slide.notes:
                            doc.send({"command": "add", "path": f"/slide[{i}]",
                                      "type": "notes", "props": {"text": slide.notes}})
                else:
                    doc.send({"command": "add", "path": "/",
                              "type": "slide", "props": {"layout": "title"}})

            doc.send({"command": "save"})

        size = os.path.getsize(path)
        return json.dumps({"status": "created", "format": params.format,
                           "path": path, "size_bytes": size,
                           "size_kb": round(size / 1024, 1)}, indent=2)
    except Exception as e:
        return json.dumps({"error": f"officecli export failed: {e}"}, indent=2)
