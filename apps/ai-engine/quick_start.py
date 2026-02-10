"""Quick start script - Minimal test"""
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'  # Fix for some Windows setups

from pipelines import TranscriptionPipeline

# Initialize (first time will download ~150MB model)
print("Initializing Whisper model...")
transcriber = TranscriptionPipeline(model_size="base")

# Get audio file
audio_file = input("Enter audio file path: ").strip()

if os.path.exists(audio_file):
    # Transcribe
    print("\nTranscribing...")
    segments = transcriber.transcribe_with_timestamps(audio_file, language="vi")
    
    # Show results
    print("\n" + "="*60)
    print("RESULTS:")
    print("="*60)
    for seg in segments:
        print(f"[{seg['start']:.1f}s] {seg['text']}")
    print("\n✅ Done!")
else:
    print(f"❌ File not found: {audio_file}")
