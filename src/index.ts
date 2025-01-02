#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ErrorCode,
  ListToolsRequestSchema,
  McpError,
} from '@modelcontextprotocol/sdk/types.js';
import axios from 'axios';
import { youtube_v3 } from '@googleapis/youtube';

class YoutubeTranscriber {
  private server: Server;
  private youtube: youtube_v3.Youtube;
  private youtubeApiKey: string;
  private gladiaApiKey: string;

  constructor(config: { env: { YOUTUBE_API_KEY: string; GLADIA_API_KEY: string } }) {
    if (!config?.env?.YOUTUBE_API_KEY || !config.env.GLADIA_API_KEY) {
      throw new Error('Les clés API YouTube et Gladia sont requises');
    }

    this.youtubeApiKey = config.env.YOUTUBE_API_KEY;
    this.gladiaApiKey = config.env.GLADIA_API_KEY;

    this.server = new Server(
      {
        name: 'youtube-transcriber',
        version: '0.1.0',
      },
      {
        capabilities: {
          resources: {},
          tools: {},
        },
      }
    );

    this.youtube = new youtube_v3.Youtube({
      auth: this.youtubeApiKey,
    });

    this.setupToolHandlers();
    this.server.onerror = (error) => console.error('[MCP Error]', error);
  }

  private setupToolHandlers() {
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: 'search_youtube_videos',
          description: 'Rechercher des vidéos YouTube',
          inputSchema: {
            type: 'object',
            properties: {
              query: {
                type: 'string',
                description: 'Termes de recherche',
              },
              maxResults: {
                type: 'number',
                description: 'Nombre maximum de résultats',
                minimum: 1,
                maximum: 50,
              },
            },
            required: ['query'],
          },
        },
        {
          name: 'transcribe_video',
          description: 'Transcrire une vidéo YouTube',
          inputSchema: {
            type: 'object',
            properties: {
              videoId: {
                type: 'string',
                description: 'ID de la vidéo YouTube',
              },
            },
            required: ['videoId'],
          },
        },
        {
          name: 'extract_key_points',
          description: 'Extraire les points clés d\'une transcription',
          inputSchema: {
            type: 'object',
            properties: {
              transcription: {
                type: 'string',
                description: 'Texte de la transcription',
              },
            },
            required: ['transcription'],
          },
        },
      ],
    }));

    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      try {
        switch (request.params.name) {
          case 'search_youtube_videos':
            return await this.handleSearchYoutubeVideos(request.params.arguments);
          case 'transcribe_video':
            return await this.handleTranscribeVideo(request.params.arguments);
          case 'extract_key_points':
            return await this.handleExtractKeyPoints(request.params.arguments);
          default:
            throw new McpError(ErrorCode.MethodNotFound, 'Outil inconnu');
        }
      } catch (error) {
        if (error instanceof Error) {
          throw new McpError(ErrorCode.InternalError, error.message);
        }
        throw new McpError(ErrorCode.InternalError, 'Une erreur inconnue est survenue');
      }
    });
  }

  private async handleSearchYoutubeVideos(args: any) {
    const response = await this.youtube.search.list({
      part: ['snippet'],
      q: args.query,
      maxResults: args.maxResults || 5,
      type: ['video'],
    });

    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify(response.data.items, null, 2),
        },
      ],
    };
  }

  private async handleTranscribeVideo(args: any) {
    const videoResponse = await this.youtube.videos.list({
      part: ['snippet'],
      id: [args.videoId],
    });

    const videoTitle = videoResponse.data.items?.[0]?.snippet?.title;

    const gladiaResponse = await axios.post(
      'https://api.gladia.io/v2/transcription/',
      {
        audio_url: `https://www.youtube.com/watch?v=${args.videoId}`,
        language: 'fr',
      },
      {
        headers: {
          'x-gladia-key': this.gladiaApiKey,
        },
      }
    );

    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify({
            videoTitle,
            transcription: gladiaResponse.data,
          }, null, 2),
        },
      ],
    };
  }

  private async handleExtractKeyPoints(args: any) {
    const keyPoints = args.transcription
      .split('.')
      .filter((s: string) => s.length > 50)
      .slice(0, 5);

    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify(keyPoints, null, 2),
        },
      ],
    };
  }

  async run() {
    const transport = new StdioServerTransport();
    
    // Gestion des erreurs de connexion
    try {
      await this.server.connect(transport);
      console.error('Serveur MCP YouTube Transcriber en cours d\'exécution');
      
      // Gestion des déconnexions
      transport.onclose = () => {
        console.error('Connexion perdue, tentative de reconnexion...');
        setTimeout(() => this.run(), 5000); // Reconnexion après 5 secondes
      };
      
      // Ping régulier pour maintenir la connexion
      setInterval(async () => {
        try {
          // Tester la connexion en envoyant une requête ping
          await this.server.ping();
        } catch (error) {
          console.error('Connexion perdue, tentative de reconnexion...');
          this.run();
        }
      }, 10000); // Vérification toutes les 10 secondes
      
    } catch (error) {
      console.error('Erreur de connexion:', error);
      setTimeout(() => this.run(), 5000); // Tentative de reconnexion après 5 secondes
    }
  }
}

// Créer et démarrer le serveur
const transcriber = new YoutubeTranscriber({
  env: {
    YOUTUBE_API_KEY: "AIzaSyAJnTxGvM8oLsUzdSTqdCntB1FB-6DI6do",
    GLADIA_API_KEY: "cf345847-680e-49a2-bfbc-eec7420dbf7b"
  }
});
transcriber.run().catch(console.error);
