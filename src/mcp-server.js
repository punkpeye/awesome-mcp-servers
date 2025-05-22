const express = require('express');
const multer = require('multer');
const path = require('path');
const { uploadFile, selectModel, displayOutput } = require('./user-interface');

const app = express();
const port = 3000;

// Set up multer for file uploads
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        const fileType = file.mimetype.split('/')[0];
        cb(null, path.join(__dirname, 'uploads', fileType));
    },
    filename: (req, file, cb) => {
        cb(null, file.originalname);
    }
});
const upload = multer({ 
    storage: storage,
    limits: { fileSize: 100 * 1024 * 1024 } // Increase file size limit to 100MB
});

// Endpoint to upload files
app.post('/upload', upload.single('file'), (req, res) => {
    const filePath = req.file.path;
    const fileType = req.file.mimetype.split('/')[0];
    uploadFile(filePath, fileType);
    res.send('File uploaded successfully');
});

// Endpoint to select model
app.post('/select-model', (req, res) => {
    const modelName = req.body.modelName;
    selectModel(modelName);
    res.send('Model selected successfully');
});

// Endpoint to display output with source links
app.post('/display-output', (req, res) => {
    const output = req.body.output;
    const sourceLinks = req.body.sourceLinks;
    displayOutput(output, sourceLinks);
    res.send('Output displayed successfully');
});

app.listen(port, () => {
    console.log(`MCP server listening at http://localhost:${port}`);
});
