# PyAudioTools

PyAudioTools is a Python library for audio format conversion and manipulation.

## Installation

You can install PyAudioTools using pip:

```bash
pip install pyaudiotools
```

## Usage

### Audio Format Conversion

To convert an audio file to a different format, use the convert_audio function:

```python
from pyaudiotools.audio_converter import convert_audio

input_file = 'input.wav'
output_file = 'output.mp3'
output_format = 'mp3'

convert_audio(input_file, output_file, output_format)
```

### Batch Conversion

To perform batch audio format conversion, use the batch_convert_audio function:

```python
from pyaudiotools.audio_converter import batch_convert_audio

input_directory = 'input_folder'
output_directory = 'output_folder'
output_format = 'ogg'

batch_convert_audio(input_directory, output_directory, output_format)

```