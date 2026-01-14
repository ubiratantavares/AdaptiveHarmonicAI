from src.service.music_xml_parser import MusicXMLParser
import os

# Sample MusicXML content (Simple C Major scale)
SAMPLE_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <part-list>
    <score-part id="P1">
      <part-name>Melody</part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1">
      <note>
        <pitch>
          <step>C</step>
          <octave>4</octave>
        </pitch>
        <duration>4</duration>
        <type>whole</type>
      </note>
    </measure>
    <measure number="2">
      <note>
        <pitch>
          <step>D</step>
          <octave>4</octave>
        </pitch>
        <duration>4</duration>
        <type>whole</type>
      </note>
    </measure>
  </part>
</score-partwise>
"""

def test_parser():
    print("Testing MusicXML Parser...")
    try:
        melody = MusicXMLParser.parse(SAMPLE_XML)
        print(f"Parsed Melody: {melody}")
        
        expected = [['C'], ['D']]
        if melody == expected:
            print("SUCCESS: Melody matches expected output.")
        else:
            print(f"FAILURE: Expected {expected}, got {melody}")
            
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    test_parser()
