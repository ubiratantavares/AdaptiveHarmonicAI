import unittest
import sys
import os
from music21 import stream

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.view.score_view import ScoreView
from src.model.models import MelodyModel, MelodyNote, DecisionLog

class TestScoreView(unittest.TestCase):
    def test_create_score(self):
        # Mock Melody
        melody_notes = [MelodyNote("C", 4, 1.0, False), MelodyNote("D", 4, 1.0, False), MelodyNote("E", 4, 1.0, False), MelodyNote("F", 4, 1.0, False)]
        melody = MelodyModel([melody_notes])
        
        # Mock Timeline
        decision = DecisionLog(
            chord_name="C", chord_key="C", function="T", chord_notes=["C", "E", "G"],
            vl_score=1.0, tension_score=1.0, function_score=1.0, total_score=1.0, justification="Test"
        )
        timeline = [decision]
        
        # Test create_score
        score = ScoreView.create_score(melody, timeline, time_signature="4/4")
        
        self.assertIsInstance(score, stream.Score)
        # Check if TimeSignature is present
        parts = score.parts
        self.assertEqual(len(parts), 2)
        
        # Check Melody Part TimeSignature
        ts_melody = parts[0].getElementsByClass('TimeSignature')[0]
        self.assertEqual(ts_melody.ratioString, "4/4")

if __name__ == '__main__':
    unittest.main()
