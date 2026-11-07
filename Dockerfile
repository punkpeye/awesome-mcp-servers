# 供 MCP 目录站（Glama 等）做 introspection 用的最小镜像。
# 本质是 stdio 客户端代理：把 stdio MCP 转发到公网 https://sanyu.wentangkeji.com/api/mcp。
# tools/list 无需 API key（目录公开）；执行动作才需要 SANYU_API_KEY。
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 \
    SANYU_BASE_URL=https://sanyu.wentangkeji.com
WORKDIR /app
COPY sanyu_mcp.py /app/sanyu_mcp.py
RUN python -c "import py_compile;py_compile.compile('/app/sanyu_mcp.py',doraise=True)"
ENTRYPOINT ["python", "/app/sanyu_mcp.py"]
