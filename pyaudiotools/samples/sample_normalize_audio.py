from pyaudiotools.normalize_audio import normalize_audio

input_audio_file = 'input.mp3'
target_volume_level = -15  # Set your target volume level in dBFS

normalized_audio = normalize_audio(input_audio_file, target_volume_level)

# Export the normalized audio to a new file
normalized_audio.export('output_normalized_audio.mp3', format='mp3')
