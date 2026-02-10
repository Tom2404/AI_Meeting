# AI Engine Setup Guide

## 🚀 Quick Start for STT & Diarization Testing

### Step 1: Install Dependencies

```bash
cd apps/ai-engine
pip install -r requirements.txt
```

**Note:** This will download ~1-2GB of packages. Be patient!

### Step 2: Get HuggingFace Token (For Diarization)

1. Go to https://huggingface.co/settings/tokens
2. Create a new token (read permission is enough)
3. Accept model terms at: https://huggingface.co/pyannote/speaker-diarization-3.1
4. Copy the token

### Step 3: Configure Environment

```bash
# Copy example env file
copy .env.example .env

# Edit .env and add your HuggingFace token
# HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxx
```

### Step 4: Prepare Test Audio

Place your audio file in:
- `data/raw_audio/test.wav` (for auto-detection)
- Or any path you'll specify when running

**Supported formats:** WAV, MP3, M4A, FLAC

### Step 5: Run Tests

```bash
# Run the test script
python test_models.py

# When prompted, either:
# - Press Enter to use default test file (data/raw_audio/test.wav)
# - Type the path to your audio file
```

## 📊 What Will Happen

### Test 1: Speech-to-Text (Whisper)
- Loads Whisper model (first time: downloads ~150MB)
- Transcribes your audio
- Shows text with timestamps

### Test 2: Speaker Diarization (Pyannote)
- Loads Pyannote model (first time: downloads ~300MB)
- Identifies different speakers
- Shows who spoke when
- Provides speaking time statistics

### Test 3: Combined Results
- Merges transcription with speaker labels
- Shows: `[SPEAKER_00]: Hello, how are you?`

## 🎯 Model Options

### Whisper Model Sizes
Edit `WHISPER_MODEL_SIZE` in `.env`:

| Model  | Size  | Speed    | Accuracy |
|--------|-------|----------|----------|
| tiny   | ~75MB | Fastest  | Good     |
| base   | ~150MB| Fast     | Better   | ⭐ Default
| small  | ~500MB| Medium   | Great    |
| medium | ~1.5GB| Slow     | Excellent|
| large  | ~3GB  | Slowest  | Best     |

**Recommendation:** Start with `base`, upgrade to `small` or `medium` if needed.

### Language Support
Whisper supports 99+ languages! Edit `DEFAULT_LANGUAGE` in `.env`:
- `vi` - Vietnamese
- `en` - English
- `ja` - Japanese
- `ko` - Korean
- `zh` - Chinese
- etc.

## 🔧 Troubleshooting

### Issue: "No module named 'whisper'"
```bash
pip install openai-whisper
```

### Issue: "No HuggingFace token"
- Diarization will be skipped
- STT will still work
- Get token from: https://huggingface.co/settings/tokens

### Issue: CUDA out of memory
Edit `.env`:
```
DEVICE=cpu
```
Or use smaller model size.

### Issue: Slow processing
- Use `tiny` or `base` model
- Use GPU if available (CUDA)
- Process shorter audio clips

## 📝 Example Output

```
TESTING SPEECH-TO-TEXT (WHISPER)
================================================
Loading Whisper model 'base' on cuda...
✓ Whisper model loaded successfully
Transcribing: test.wav...

📝 Transcription Results (5 segments):

[00:00 -> 00:05] Xin chào mọi người, hôm nay chúng ta sẽ họp
[00:05 -> 00:10] Vâng, tôi nghĩ chúng ta nên bắt đầu
[00:10 -> 00:15] Được rồi, việc đầu tiên là...

TESTING SPEAKER DIARIZATION (PYANNOTE)
================================================
Loading Pyannote diarization pipeline on cuda...
✓ Diarization pipeline loaded successfully

👥 Speaker Segments (15 segments):

[00:00 -> 00:05] SPEAKER_00
[00:05 -> 00:10] SPEAKER_01
[00:10 -> 00:15] SPEAKER_00

📊 Speaker Statistics:

SPEAKER_00: 2m 30s (8 segments)
SPEAKER_01: 1m 45s (7 segments)

COMBINED RESULTS (STT + DIARIZATION)
================================================

💬 Conversation with Speakers:

[00:00] SPEAKER_00: Xin chào mọi người, hôm nay chúng ta sẽ họp
[00:05] SPEAKER_01: Vâng, tôi nghĩ chúng ta nên bắt đầu
[00:10] SPEAKER_00: Được rồi, việc đầu tiên là...
```

## 🎓 Next Steps

Once testing works:
1. Integrate with backend via gRPC/RabbitMQ
2. Add real-time processing
3. Implement translation pipeline
4. Add summarization with LLM

## 💡 Tips

- **First run is slow** (downloads models) - subsequent runs are fast
- **GPU recommended** but CPU works fine for short clips
- **Audio quality matters** - clear audio = better results
- **Vietnamese works great** with Whisper!
