from pyaudiotoolbox.audio_editor import trim_audio, split_audio, concatenate_audio, apply_fade_in, apply_fade_out

# Trim audio from 10 seconds to 30 seconds
input_audio = "input.mp3"
output_audio = "trimmed_output.mp3"
start_time_ms = 10000  # 10 seconds
end_time_ms = 30000    # 30 seconds

trim_audio(input_audio, output_audio, start_time_ms, end_time_ms)


# Split audio into segments at 10 seconds and 20 seconds
input_audio = "input.mp3"
output_prefix = "segment"
split_points_ms = [10000, 20000]

split_audio(input_audio, output_prefix, split_points_ms)

# Concatenate two audio files into one
input_files = ["input.mp3", "segment_1.mp3"]
output_audio = "concatenated_output.mp3"

concatenate_audio(input_files, output_audio)

# Apply a 3-second fade-in effect to an audio file
input_audio = "input.mp3"
output_audio = "faded_input.mp3"
fade_duration_ms = 3000  # 3 seconds

apply_fade_in(input_audio, output_audio, fade_duration_ms)

# Apply a 2-second fade-out effect to an audio file
input_audio = "input.mp3"
output_audio = "faded_output.mp3"
fade_duration_ms = 2000  # 2 seconds

apply_fade_out(input_audio, output_audio, fade_duration_ms)
