# AI Engine - STT & Diarization

AI processing engine for Speech-to-Text, Speaker Diarization, and Translation.

## 🎯 Quick Start (3 Steps!)

### 1️⃣ Install Dependencies
```powershell
cd apps/ai-engine
pip install -r requirements.txt
```
⏱️ Takes 5-10 minutes. Models will download on first run.

### 2️⃣ Setup Environment (Optional for Diarization)
```powershell
copy .env.example .env
# Edit .env and add your HuggingFace token for speaker diarization
```


### 3️⃣ Run Tests
```powershell
# Quick test (STT only)
python quick_start.py

# Full test (STT + Diarization)
python test_models.py
```

## 📚 What's Inside

```
ai-engine/
├── pipelines/           # AI processing pipelines
│   ├── transcription.py # Whisper STT
│   ├── diarization.py   # Pyannote speaker ID
│   └── translation.py   # (Coming soon)
├── models/              # Model storage (auto-created)
├── utils/               # Helper functions
├── test_models.py       # Comprehensive test script
├── quick_start.py       # Minimal test script
└── SETUP.md            # Detailed setup guide
```

## 🔑 Key Features

### Speech-to-Text (Whisper)
- ✅ 99+ languages supported
- ✅ High accuracy for Vietnamese
- ✅ Automatic timestamps
- ✅ Works offline
- ✅ Multiple model sizes (tiny → large)

### Speaker Diarization (Pyannote)
- ✅ Identifies multiple speakers
- ✅ Speaker timestamps
- ✅ Speaking time statistics
- ✅ Auto-detects speaker count
- ⚠️ Requires HuggingFace token

## 🎮 Usage Examples

### Example 1: Basic Transcription
```python
from pipelines import TranscriptionPipeline

# Initialize
transcriber = TranscriptionPipeline(model_size="base")

# Transcribe
segments = transcriber.transcribe_with_timestamps("audio.wav", language="vi")

for seg in segments:
    print(f"[{seg['start']:.1f}s] {seg['text']}")
```

### Example 2: Speaker Diarization
```python
from pipelines import DiarizationPipeline
import os

# Initialize (requires HF_TOKEN environment variable)
diarizer = DiarizationPipeline(hf_token=os.getenv("HF_TOKEN"))

# Analyze speakers
segments = diarizer.diarize("audio.wav", num_speakers=2)

for seg in segments:
    print(f"{seg['speaker']}: {seg['start']:.1f}s - {seg['end']:.1f}s")
```

### Example 3: Combined (STT + Diarization)
```python
from pipelines import TranscriptionPipeline, DiarizationPipeline

# Initialize both
transcriber = TranscriptionPipeline(model_size="base")
diarizer = DiarizationPipeline()

# Process audio
text_segments = transcriber.transcribe_with_timestamps("meeting.wav")
speaker_segments = diarizer.diarize("meeting.wav")

# Combine results...
# (See test_models.py for full implementation)
```

## 🚀 Model Performance

### Whisper Models

| Model  | Size   | Speed      | RAM    | Accuracy |
|--------|--------|------------|--------|----------|
| tiny   | 75 MB  | ~10x faster| 1 GB   | ⭐⭐⭐   |
| base   | 150 MB | ~7x faster | 1 GB   | ⭐⭐⭐⭐ |
| small  | 500 MB | ~4x faster | 2 GB   | ⭐⭐⭐⭐⭐ |
| medium | 1.5 GB | ~2x faster | 5 GB   | ⭐⭐⭐⭐⭐ |
| large  | 3 GB   | baseline   | 10 GB  | ⭐⭐⭐⭐⭐ |

**Recommended:** Start with `base`, upgrade if needed.

### Processing Speed (on CPU)
- 1 minute audio ≈ 30-60 seconds processing (base model)
- GPU: 5-10x faster

## 🛠️ Troubleshooting

### "ModuleNotFoundError: No module named 'whisper'"
```powershell
pip install openai-whisper
```

### "No HuggingFace token provided"
- Speaker diarization requires HF token
- Get it from: https://huggingface.co/settings/tokens
- Accept terms: https://huggingface.co/pyannote/speaker-diarization-3.1
- Add to `.env` file: `HF_TOKEN=hf_xxxxx`

### Slow processing / Out of memory
```python
# Use smaller model
transcriber = TranscriptionPipeline(model_size="tiny")

# Or use CPU explicitly
transcriber = TranscriptionPipeline(model_size="base", device="cpu")
```

### Audio quality issues
- Use clear audio (minimal background noise)
- Prefer WAV format over MP3
- 16kHz sample rate recommended
- Mono channel preferred

## 📖 Next Steps

1. ✅ **You are here**: Test STT & Diarization
2. ⏭️ Add translation pipeline
3. ⏭️ Integrate with backend (gRPC/RabbitMQ)
4. ⏭️ Add real-time streaming
5. ⏭️ Deploy with Docker

## 📚 Resources

- **Whisper**: https://github.com/openai/whisper
- **Pyannote**: https://github.com/pyannote/pyannote-audio
- **Full Setup Guide**: See [SETUP.md](SETUP.md)

## 💬 Support

Having issues? Check:
1. [SETUP.md](SETUP.md) for detailed instructions
2. Requirements are installed: `pip list | grep -E "whisper|pyannote|torch"`
3. Audio file exists and is readable
4. HF_TOKEN is set (for diarization)

---

**Happy Testing! 🎉**
