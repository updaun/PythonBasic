import re

p = re.compile('[a-z]+')

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

# 정규표현식 연습 사이트
# regexr.com

# [a-zA-Z] 
# . 전체
# * 반복  [To]*  Too
# + 앞에 있는 글자를 최소 1회 이상 반복
# {} 반복 횟수 지정 [A-Za-z]{3} 영어 대소문자 3글자
# {m.n} - 반복 횟수 지정 {1,} {0,} {1,3}
# 203.252.101.40  [0-9]{1,3}    \d{1,3}
# ? 반복횟수가 1회
# 010-0000-0000     01[01]?-[0-9]{4}-[0-9]{4}
# | or (0|1){3}
# ^ not

# (http)(.+)(zip)

# [a-zA-Z0-9]+\*\*\*

import re
import urllib.request

url = "https://bit.ly/3rxQFS4"
html = urllib.request.urlopen(url)
html_contents = str(html.read())
id_results = re.findall(r"([a-zA-Z0-9]+\*\*\*)", html_contents)

for result in id_results:
    print(result)


url = "http://www.google.com/googlebooks/uspto-patents-grants-text.html"

html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("utf8"))

url_list = re.findall(r"(http)(.+)(zip)", html_contents)
for url in url_list:
    print("".join(url))