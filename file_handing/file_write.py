# w 는 파일 덮어쓰기
f = open("file_handing/count_log.txt", "w", encoding="utf8")
for i in range(1, 11):
    data = "{0}번째 줄입니다. \n".format(i)
    f.write(data)
f.close()

# a 파일에 계속 연속해서 쓰기 : append
f = open("file_handing/count_log.txt", "a", encoding="utf8")
for i in range(11, 21):
    data = "{0}번째 줄입니다. \n".format(i)
    f.write(data)
f.close()