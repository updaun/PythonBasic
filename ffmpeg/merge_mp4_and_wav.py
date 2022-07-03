import os

input_video_path = 'test_video.mp4'
input_audio_path = 'test_video.wav'

output_video_path = 'output.mp4'

# merge mp4 and wav
os.system(f"ffmpeg -hide_banner -loglevel error -y -i {input_video_path} -i {input_audio_path} -c:v copy -c:a aac {output_video_path}")