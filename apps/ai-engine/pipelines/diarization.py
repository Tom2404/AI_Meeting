"""Agent Speaker: Identify and separate speakers using Pyannote"""
from pyannote.audio import Pipeline
import torch
from typing import List, Dict, Optional
import os


class DiarizationPipeline:
    """Speaker Diarization using Pyannote.audio"""
    
    def __init__(self, hf_token: Optional[str] = None, device: Optional[str] = None):
        """
        Initialize Pyannote diarization pipeline
        
        Args:
            hf_token: HuggingFace token (required for pyannote models)
            device: Device to run on (cuda/cpu). Auto-detected if None
        """
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.hf_token = hf_token or os.getenv("HF_TOKEN")
        
        if not self.hf_token:
            print("⚠️  Warning: No HuggingFace token provided. Set HF_TOKEN env variable.")
            print("   Get token from: https://huggingface.co/settings/tokens")
            print("   Accept pyannote/speaker-diarization terms: https://huggingface.co/pyannote/speaker-diarization")
            self.pipeline = None
        else:
            print(f"Loading Pyannote diarization pipeline on {self.device}...")
            try:
                self.pipeline = Pipeline.from_pretrained(
                    "pyannote/speaker-diarization-3.1",
                    use_auth_token=self.hf_token
                )
                self.pipeline.to(torch.device(self.device))
                print(f"✓ Diarization pipeline loaded successfully")
            except Exception as e:
                print(f"❌ Error loading pipeline: {e}")
                self.pipeline = None
    
    def diarize(self, audio_path: str, num_speakers: Optional[int] = None) -> List[Dict]:
        """
        Perform speaker diarization on audio file
        
        Args:
            audio_path: Path to audio file
            num_speakers: Expected number of speakers (None = auto-detect)
            
        Returns:
            List of speaker segments with start/end times and speaker labels
        """
        if not self.pipeline:
            print("❌ Diarization pipeline not initialized. Check HF_TOKEN.")
            return []
        
        print(f"Analyzing speakers in: {audio_path}...")
        
        # Run diarization
        diarization = self.pipeline(
            audio_path,
            num_speakers=num_speakers
        )
        
        # Extract segments
        segments = []
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            segments.append({
                "start": turn.start,
                "end": turn.end,
                "speaker": speaker
            })
        
        return segments
    
    def get_speaker_stats(self, segments: List[Dict]) -> Dict:
        """
        Calculate speaking time statistics for each speaker
        
        Args:
            segments: List of speaker segments
            
        Returns:
            Dictionary with speaker statistics
        """
        stats = {}
        for seg in segments:
            speaker = seg["speaker"]
            duration = seg["end"] - seg["start"]
            
            if speaker not in stats:
                stats[speaker] = {
                    "total_time": 0,
                    "segments": 0
                }
            
            stats[speaker]["total_time"] += duration
            stats[speaker]["segments"] += 1
        
        return stats
