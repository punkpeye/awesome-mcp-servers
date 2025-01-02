# YouTube Transcriber MCP Server

## Overview
This MCP (Model Context Protocol) server provides powerful tools for working with YouTube videos:
1. Search YouTube videos
2. Transcribe video audio using Gladia's state-of-the-art speech recognition
3. Extract key points from transcriptions

## Why Gladia?
Gladia offers several advantages for audio transcription:
- **High Accuracy**: State-of-the-art speech recognition models
- **Multi-language Support**: Transcribe videos in multiple languages
- **Fast Processing**: Quick turnaround times for transcriptions
- **Speaker Diarization**: Identify different speakers in the audio
- **Punctuation & Formatting**: Clean, readable transcriptions
- **Free for 10 hours each month**: More than enough for most users

## Installation
1. Clone this repository
2. Install dependencies:
   ```bash
   npm install
   ```
3. Build the project:
   ```bash
   npm run build
   ```

## Configuration
To use your own API keys:

1. **YouTube API Key**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the YouTube Data API v3
   - Create credentials and get your API key

2. **Gladia API Key**
   - Sign up at [Gladia.io](https://gladia.io/)
   - Get your API key from the dashboard

3. Add the API keys to your Claude Desktop configuration:
   Edit the `claude_desktop_config.json` file (usually located in `C:\Users\gener\AppData\Roaming\Claude`) and add the following section under `mcpServers`:
   ```json
   "dtube-transcriber": {
     "command": "node",
     "args": [
       "C:\\Users\\gener\\Documents\\Cline\\MCP\\youtube-transcriber\\build\\index.js"
     ],
     "env": {
       "YOUTUBE_API_KEY": "your_youtube_api_key",
       "GLADIA_API_KEY": "your_gladia_api_key"
     }
   }
   ```

## Usage
### Search YouTube Videos
```json
{
  "name": "search_youtube_videos",
  "arguments": {
    "query": "search terms",
    "maxResults": 5
  }
}
```

### Transcribe Video
```json
{
  "name": "transcribe_video",
  "arguments": {
    "videoId": "YouTube_video_id"
  }
}
```

### Extract Key Points
```json
{
  "name": "extract_key_points",
  "arguments": {
    "transcription": "transcription_text"
  }
}
```

## Examples
### Search Example
```bash
curl -X POST http://localhost:3000/tools -d '{
  "name": "search_youtube_videos",
  "arguments": {
    "query": "AI technology",
    "maxResults": 3
  }
}'
```

### Transcribe Example
```bash
curl -X POST http://localhost:3000/tools -d '{
  "name": "transcribe_video",
  "arguments": {
    "videoId": "dQw4w9WgXcQ"
  }
}'
```

## Contributing
Contributions are welcome! Please open an issue or pull request on GitHub.

## Made by
Théo DESROUSSEAUX

## License
MIT License
