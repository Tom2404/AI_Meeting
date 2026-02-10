# Test Audio Files

Place your audio files here for testing.

## Recommended Format
- **Format:** WAV or MP3
- **Sample Rate:** 16kHz (16000 Hz)
- **Channels:** Mono (1 channel) or Stereo
- **Duration:** 30 seconds to 5 minutes for testing

## File Naming
- `test.wav` - Default test file (used by test_models.py)
- `meeting_sample_1.wav` - Meeting recording sample
- `interview_vi.mp3` - Vietnamese interview

## How to Get Test Audio

### Option 1: Record Your Own
Use your phone or computer to record a short conversation or meeting.

### Option 2: Convert from MP3 to WAV (if needed)
```bash
# Using ffmpeg
ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav
```

### Option 3: Use Online Test Files
Download sample audio from:
- https://www.voiptroubleshooter.com/open_speech/
- https://commons.wikimedia.org/wiki/Category:Audio_files_of_speeches

## For Vietnamese Testing
Record yourself or friends having a short conversation (1-2 minutes) about any topic.
