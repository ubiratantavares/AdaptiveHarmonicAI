import unittest
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.service.music_xml_parser import MusicXMLParser

class TestMusicXMLParser(unittest.TestCase):
    def test_parse_simple_xml(self):
        # Minimal valid MusicXML with one measure and one note (C4)
        xml_content = b"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <part-list>
    <score-part id="P1">
      <part-name>Music</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <attributes>
        <divisions>1</divisions>
        <key>
          <fifths>0</fifths>
        </key>
        <time>
          <beats>4</beats>
          <beat-type>4</beat-type>
        </time>
        <clef>
          <sign>G</sign>
          <line>2</line>
        </clef>
      </attributes>
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>4</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
"""
        result = MusicXMLParser.parse(xml_content)
        self.assertIsInstance(result, dict)
        self.assertIn("measures", result)
        self.assertIn("time_signature", result)
        self.assertEqual(len(result["measures"]), 1)
        
        # Check first note
        first_note = result["measures"][0][0]
        self.assertEqual(first_note.name, 'C')
        self.assertEqual(first_note.octave, 4)
        self.assertEqual(first_note.duration, 4.0)
        self.assertFalse(first_note.is_rest)
        
        self.assertEqual(result["time_signature"], "4/4")
        # Music21 default metadata might be empty or specific defaults, check keys exist
        self.assertIn("title", result)
        self.assertIn("composer", result)

if __name__ == '__main__':
    unittest.main()
