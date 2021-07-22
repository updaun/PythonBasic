import requests
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env_list = dict()
local_env = open(os.path.join(BASE_DIR,'.env'))

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', "")
    start = line.find("=")
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value

city = "Seoul"
API_KEY = env_list["API_KEY"]
lang = "kr"

api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={API_KEY}&lang={lang}&units=metric"""
# &lang={lang} 언어 변경
# &units=metric 온도 단위 변경

result = requests.get(api)

# print(result.text)

data = json.loads(result.text)

# print(type(result.text)) # str

# print(type(data)) # dict

# 지역
print(data["name"], "날씨입니다.")
# 날씨
print("날씨는", data["weather"][0]["main"], "입니다.")
print("날씨는", data["weather"][0]["description"], "입니다.")
# 온도
print("현재 온도는", data["main"]["temp"],"입니다.")
# 체감 온도
print("체감 온도는", data["main"]["feels_like"],"입니다.")
# 최저 기온
print("최저 기온는", data["main"]["temp_min"],"입니다.")
# 최고 기온
print("최저 기온는", data["main"]["temp_max"],"입니다.")
# 습도
print("습도는", data["main"]["humidity"],"입니다.")
# 기압
print("기압은", data["main"]["pressure"],"입니다.")
# 풍향
print("풍향은", data["wind"]["deg"],"입니다.")
# 풍속
print("풍속은", data["wind"]["speed"],"입니다.")