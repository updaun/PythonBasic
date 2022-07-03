import os

start_time = 10
end_time = 30

input_audio_path = 'origin_video.mp3'
output_audio_path = 'test_video.mp3'

# 오디오 자르기
os.system(f'ffmpeg -y -i {input_audio_path} -ss {start_time} -to {end_time} -acodec copy {output_audio_path}')