# Sample code for convert_audio, batch_convert_audio
from pyaudiotoolbox.audio_converter import convert_audio, batch_convert_audio

# Test individual audio conversion
input_audio = 'input.mp3'
output_audio = 'output.wav'
output_format = 'wav'

convert_audio(input_audio, output_audio, output_format)

# # Test batch audio conversion
input_dir = 'input_folder'
output_dir = 'output_folder'
output_format = 'ogg'

batch_convert_audio(input_dir, output_dir, output_format)
