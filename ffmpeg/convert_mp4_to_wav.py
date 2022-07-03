import os

input_video_path = 'origin_video.mp4'

output_audio_path = 'test_video.wav'

# mp4 to wav
os.system(f'ffmpeg -hide_banner -loglevel error -y -i {input_video_path} -ab 160K -ac 1 -ar 16000 -vn {output_audio_path}')