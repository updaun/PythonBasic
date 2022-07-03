import os

start_time = 10
end_time = 30

input_video_path = 'origin_video.mp4'
output_video_path = 'test_video.mp4'

# 비디오 자르기
os.system(f'ffmpeg -y -i {input_video_path} -ss {start_time} -to {end_time} -vcodec copy -acodec copy {output_video_path}')
