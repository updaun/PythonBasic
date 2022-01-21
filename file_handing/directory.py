import os

from itsdangerous import exc
from numpy import source

# 디렉토리 생성
# os.mkdir("file_handing/log")

# 디렉토리 생성 예외처리
try:
    os.mkdir("file_handing/log")
except FileExistsError as e:
    print("Already created")

# 디렉토리 존재 여부 확인
print(os.path.exists("file_handing/log"))

# isfile
print(os.path.isfile("file_handing/test.txt"))

# isdir
print(os.path.isdir("file_handing/log"))



# file 옮기기
import shutil

source = "file_handing/test.txt"
dest = os.path.join("file_handing", "log\\test.txt")

shutil.copy(source, dest)

# pathlib 모듈 사용으로 path를 객체로 다룸
import pathlib

cwd = pathlib.Path.cwd()
print(cwd)

print(cwd.parent)

print(list(cwd.parent.parents))

print(list(cwd.glob("*")))