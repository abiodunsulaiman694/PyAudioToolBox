import unittest
from unittest.mock import patch, Mock
from pyaudiotools.audio_extractor import extract_audio

class MockVideoFileClip:

    def __init__(self, *args, **kwargs):
        self.audio = Mock()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

@patch('pyaudiotools.audio_extractor.VideoFileClip', MockVideoFileClip)
class TestAudioExtractor(unittest.TestCase):

    def test_extract_audio_default(self):
        input_video = 'test_input.mp4'
        output_audio = 'test_output.wav'

        # Test audio extraction
        extract_audio(input_video, output_audio)

        # Perform any assertions you need to verify the outcome
        # For example, you can check if the output audio file exists and has the expected properties.

if __name__ == '__main__':
    unittest.main()
