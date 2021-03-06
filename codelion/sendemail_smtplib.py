from email import message
import smtplib
from email.message import EmailMessage
import os
from pathlib import Path
import imghdr
import re

BASE_DIR = Path(__file__).resolve().parent.parent

google_list = dict()
local_env = open(os.path.join(BASE_DIR,'.google_info'))

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', "")
    start = line.find("=")
    key = line[:start]
    value = line[start+1:]
    google_list[key] = value

GOOGLE_ID = google_list["GOOGLE_ID"]
GOOGLE_PASSWORD = google_list["GOOGLE_PASSWORD"]
OTHER_ID = google_list["OTHER_ID"]

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    # 이메일 유효성 검사 - 정규표현식
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)):
        # 메일 보내기
        smtp.send_message(message)
        print("정상적으로 메일이 전송 되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

# 메세지 생성
message = EmailMessage()
# 메세지 본문
message.set_content("안녕하세요. 만나서 반갑습니다. https://github.com/updaun 로 놀러오세요!")
# 메세지 제목
message["Subject"] = "[Updaun] 제 Github로 초대합니다."
# 메세지 보내는 사람
message["From"] = str(GOOGLE_ID)
# 메세지 받는 사람
message["To"] = str(OTHER_ID)

# 이미지 파일 읽기
# image = open("codelion/image/walle.jpg", "rb")
# image.read()

# 이미지 파일 읽기(with)
with open("codelion/image/walle.jpg", "rb") as image:
    image_file = image.read()

# 이미지 확장자 알기
image_type = imghdr.what('walle', image_file)

# 이미지 파일을 메일에 포함시키기
message.add_attachment(image_file, maintype='image',subtype=image_type)

# 서버에 연결
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

# 로그인 테스트
print(smtp.login(GOOGLE_ID, GOOGLE_PASSWORD))

# 로그인
smtp.login(GOOGLE_ID, GOOGLE_PASSWORD)

# 메일을 보내는 sendEmail 함수 호출 및 실행
sendEmail(str(OTHER_ID))

smtp.quit()