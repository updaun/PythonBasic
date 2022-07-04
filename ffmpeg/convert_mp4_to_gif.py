import os

file_path = 'test2.mp4'

os.system(f'ffmpeg -y -ss 17 -t 10 -i {file_path} -vf "fps=10,scale=550:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 {file_path[:-4]}.gif')

