"""Test script for STT and Diarization models"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add pipelines to path
sys.path.append(str(Path(__file__).parent))

from pipelines.transcription import TranscriptionPipeline
from pipelines.diarization import DiarizationPipeline

# Load environment variables
load_dotenv()


def test_transcription(audio_path: str):
    """Test Speech-to-Text transcription"""
    print("\n" + "="*60)
    print("TESTING SPEECH-TO-TEXT (WHISPER)")
    print("="*60)
    
    # Initialize transcription pipeline
    model_size = os.getenv("WHISPER_MODEL_SIZE", "base")
    transcriber = TranscriptionPipeline(model_size=model_size)
    
    # Transcribe audio
    language = os.getenv("DEFAULT_LANGUAGE", "vi")
    segments = transcriber.transcribe_with_timestamps(audio_path, language=language)
    
    # Display results
    print(f"\n📝 Transcription Results ({len(segments)} segments):\n")
    for i, seg in enumerate(segments, 1):
        start_time = f"{int(seg['start']//60):02d}:{int(seg['start']%60):02d}"
        end_time = f"{int(seg['end']//60):02d}:{int(seg['end']%60):02d}"
        print(f"[{start_time} -> {end_time}] {seg['text']}")
    
    return segments


def test_diarization(audio_path: str):
    """Test Speaker Diarization"""
    print("\n" + "="*60)
    print("TESTING SPEAKER DIARIZATION (PYANNOTE)")
    print("="*60)
    
    # Initialize diarization pipeline
    hf_token = os.getenv("HF_TOKEN")
    diarizer = DiarizationPipeline(hf_token=hf_token)
    
    if not diarizer.pipeline:
        print("\n⚠️  Diarization skipped (no HF_TOKEN)")
        return []
    
    # Perform diarization
    segments = diarizer.diarize(audio_path, num_speakers=None)
    
    # Display results
    print(f"\n👥 Speaker Segments ({len(segments)} segments):\n")
    for i, seg in enumerate(segments[:20], 1):  # Show first 20
        start_time = f"{int(seg['start']//60):02d}:{int(seg['start']%60):02d}"
        end_time = f"{int(seg['end']//60):02d}:{int(seg['end']%60):02d}"
        print(f"[{start_time} -> {end_time}] {seg['speaker']}")
    
    if len(segments) > 20:
        print(f"... and {len(segments) - 20} more segments")
    
    # Show statistics
    stats = diarizer.get_speaker_stats(segments)
    print(f"\n📊 Speaker Statistics:\n")
    for speaker, data in stats.items():
        minutes = int(data['total_time'] // 60)
        seconds = int(data['total_time'] % 60)
        print(f"{speaker}: {minutes}m {seconds}s ({data['segments']} segments)")
    
    return segments


def combine_transcription_and_diarization(transcription_segments, diarization_segments):
    """Combine STT and diarization results"""
    print("\n" + "="*60)
    print("COMBINED RESULTS (STT + DIARIZATION)")
    print("="*60)
    
    if not diarization_segments:
        print("\n⚠️  No diarization data to combine")
        return
    
    print("\n💬 Conversation with Speakers:\n")
    
    for trans_seg in transcription_segments:
        # Find overlapping speaker
        trans_start = trans_seg['start']
        trans_end = trans_seg['end']
        
        # Find speaker who spoke most during this segment
        speaker_times = {}
        for dia_seg in diarization_segments:
            # Calculate overlap
            overlap_start = max(trans_start, dia_seg['start'])
            overlap_end = min(trans_end, dia_seg['end'])
            overlap = max(0, overlap_end - overlap_start)
            
            if overlap > 0:
                speaker = dia_seg['speaker']
                speaker_times[speaker] = speaker_times.get(speaker, 0) + overlap
        
        # Get dominant speaker
        if speaker_times:
            dominant_speaker = max(speaker_times, key=speaker_times.get)
        else:
            dominant_speaker = "UNKNOWN"
        
        # Display
        start_time = f"{int(trans_start//60):02d}:{int(trans_start%60):02d}"
        print(f"[{start_time}] {dominant_speaker}: {trans_seg['text']}")


def main():
    """Main test function"""
    print("\n🚀 AI Meeting - STT & Diarization Test")
    print("="*60)
    
    # Check for audio file
    audio_path = input("\n📁 Enter path to audio file (or press Enter for demo): ").strip()
    
    if not audio_path:
        # Check if demo file exists
        demo_path = Path(__file__).parent.parent.parent / "data" / "raw_audio" / "test.wav"
        if demo_path.exists():
            audio_path = str(demo_path)
            print(f"✓ Using demo file: {audio_path}")
        else:
            print(f"\n❌ No audio file provided and demo not found at: {demo_path}")
            print("\nPlease provide an audio file path (.wav, .mp3, etc.)")
            return
    
    if not os.path.exists(audio_path):
        print(f"\n❌ File not found: {audio_path}")
        return
    
    try:
        # Test transcription
        transcription_segments = test_transcription(audio_path)
        
        # Test diarization
        diarization_segments = test_diarization(audio_path)
        
        # Combine results
        if transcription_segments and diarization_segments:
            combine_transcription_and_diarization(transcription_segments, diarization_segments)
        
        print("\n" + "="*60)
        print("✅ Testing completed successfully!")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
