"""Agent Transcriber: Convert Speech -> Text using Whisper"""
import whisper
import torch
import numpy as np
from typing import Dict, Optional
import os


class TranscriptionPipeline:
    """Speech-to-Text using OpenAI Whisper model"""
    
    def __init__(self, model_size: str = "base", device: Optional[str] = None):
        """
        Initialize Whisper model for transcription
        
        Args:
            model_size: Model size (tiny, base, small, medium, large)
            device: Device to run on (cuda/cpu). Auto-detected if None
        """
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Loading Whisper model '{model_size}' on {self.device}...")
        self.model = whisper.load_model(model_size, device=self.device)
        print(f"✓ Whisper model loaded successfully")
    
    def transcribe(self, audio_path: str, language: str = "vi") -> Dict:
        """
        Transcribe audio file to text
        
        Args:
            audio_path: Path to audio file
            language: Language code (vi=Vietnamese, en=English, etc.)
            
        Returns:
            Dictionary with transcription results
        """
        print(f"Transcribing: {audio_path}...")
        
        result = self.model.transcribe(
            audio_path,
            language=language,
            verbose=False,
            task="transcribe"
        )
        
        return {
            "text": result["text"],
            "segments": result["segments"],
            "language": result["language"]
        }
    
    def transcribe_with_timestamps(self, audio_path: str, language: str = "vi") -> list:
        """
        Transcribe with detailed timestamps for each segment
        
        Returns:
            List of segments with start/end times and text
        """
        result = self.transcribe(audio_path, language)
        
        segments = []
        for seg in result["segments"]:
            segments.append({
                "start": seg["start"],
                "end": seg["end"],
                "text": seg["text"].strip()
            })
        
        return segments
