# AI Meeting - Real-time Meeting Transcription & Analysis

## Project Overview
An AI-powered meeting assistant that provides real-time transcription, speaker diarization, translation, and intelligent meeting summaries.

## Architecture

### 🤖 Apps
The project consists of 3 main applications:

#### 1. **ai-engine/** (Python - Heavy Processing)
- **models/**: AI Model loading
  - `whisper/`: Speech-to-Text (Quantized)
  - `pyannote/`: Speaker Diarization
  - `llm/`: Summarization (Llama/Mistral local or API)
- **pipelines/**: Processing workflows
  - `transcription.py`: Speech → Text
  - `diarization.py`: Speaker identification
  - `translation.py`: Multi-language support
- **utils/**: Audio preprocessing
  - `audio_cleaner.py`: Noise reduction
- `main.py`: gRPC/Queue worker entry point

#### 2. **backend/** (FastAPI - Python)
- **core/**: System configuration
  - `config.py`: Environment variables
  - `security.py`: JWT/OAuth2
- **modules/**: Feature modules
  - `auth/`: User authentication
  - `meeting/`: CRUD operations
  - `websocket/`: Real-time communication
  - `summary/`: Meeting summaries
- **database/**: PostgreSQL with SQLAlchemy
- `main.py`: API server entry point

#### 3. **web-client/** (React/Next.js)
- **components/**: UI components
  - `Meeting/Subtitle.tsx`: Live subtitles
  - `Meeting/AudioViz.tsx`: Audio visualization
- **hooks/**: Custom React hooks
  - `useWebSocket.ts`: Real-time connection
  - `useRecorder.ts`: Browser audio recording
- **workers/**: Web Workers
  - `vad-processor.js`: Voice activity detection
- **services/**: API integration (Axios/Fetch)
- **app/**: Routing (Dashboard, Login, Meeting Room)

### 🏗️ Infrastructure
- `docker-compose.yml`: Orchestrates all 3 apps
- `nginx/`: Load balancer & reverse proxy
- `rabbitmq/`: Message queue for AI backend

### 📊 Data
- `raw_audio/`: Test audio files
- `transcripts/`: ASR results
- `prompts/`: LLM prompt engineering

### 📚 Documentation
- `architecture/`: System diagrams (Draw.io)
- `api-specs/`: OpenAPI/Swagger specs
- `sprints/`: Sprint logs (1-18)

## Tech Stack

**AI Engine:**
- Python, PyTorch, Transformers
- Whisper (STT), Pyannote (Diarization)
- Llama/Mistral (Summarization)

**Backend:**
- FastAPI, PostgreSQL, SQLAlchemy
- WebSocket, gRPC, RabbitMQ
- JWT/OAuth2

**Frontend:**
- React, Next.js, TypeScript
- WebSocket, Web Workers
- Audio recording & visualization

**DevOps:**
- Docker, Docker Compose
- Nginx, RabbitMQ

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- Docker & Docker Compose

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd AI_Meeting

# Setup AI Engine
cd apps/ai-engine
pip install -r requirements.txt

# Setup Backend
cd ../backend
pip install -r requirements.txt

# Setup Frontend
cd ../web-client
npm install

# Run with Docker
cd ../../infrastructure
docker-compose up
```

## Project Status
Sprint 1-18 documentation available in `docs/sprints/`

## License
[Your License Here]