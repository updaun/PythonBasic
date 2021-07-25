from email import message
import smtplib
from email.message import EmailMessage
import os
from pathlib import Path

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
image = open("codelion/image/walle.jpg", "rb")

image.read()
# 서버에 연결
# smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

# 로그인 테스트
# print(smtp.login(GOOGLE_ID, GOOGLE_PASSWORD))

# 로그인
# smtp.login(GOOGLE_ID, GOOGLE_PASSWORD)

# 메일 보내기
# smtp.send_message(message)
# print("메일 전송 완료!")
# smtp.quit()