const fs = require('fs');
const path = require('path');

// Configuration file for paths and other constants
const config = {
    uploadDir: path.join(__dirname, 'uploads'),
    errorLog: path.join(__dirname, 'error.log')
};

// Function to log errors to a file
function logError(error) {
    const errorMessage = `${new Date().toISOString()} - ${error}\n`;
    fs.appendFile(config.errorLog, errorMessage, (err) => {
        if (err) {
            console.error('Error logging to file:', err);
        }
    });
}

// Function to upload files
async function uploadFile(filePath, fileType) {
    const fileName = path.basename(filePath);
    const destination = path.join(config.uploadDir, fileType, fileName);

    try {
        await fs.promises.copyFile(filePath, destination);
        console.log('File uploaded successfully:', fileName);
    } catch (error) {
        console.error('Error uploading file:', error);
        logError(error);
    }
}

// Function to select model
function selectModel(modelName) {
    console.log('Model selected:', modelName);
    // Add logic to handle model selection
}

// Function to display output with source links
function displayOutput(output, sourceLinks) {
    console.log('Output:', output);
    console.log('Source Links:', sourceLinks);
}

// Function to delete uploaded files
async function deleteFile(filePath) {
    try {
        await fs.promises.unlink(filePath);
        console.log('File deleted successfully:', filePath);
    } catch (error) {
        console.error('Error deleting file:', error);
        logError(error);
    }
}

// Function to list all uploaded files
async function listFiles(fileType) {
    const directory = path.join(config.uploadDir, fileType);
    try {
        const files = await fs.promises.readdir(directory);
        return files;
    } catch (error) {
        console.error('Error listing files:', error);
        logError(error);
        return [];
    }
}

// Function to update metadata of uploaded files
async function updateMetadata(filePath, metadata) {
    try {
        await fs.promises.writeFile(`${filePath}.metadata.json`, JSON.stringify(metadata, null, 2));
        console.log('Metadata updated successfully:', filePath);
    } catch (error) {
        console.error('Error updating metadata:', error);
        logError(error);
    }
}

module.exports = {
    uploadFile,
    selectModel,
    displayOutput,
    deleteFile,
    listFiles,
    updateMetadata
};
