import os

directory_path = "file_handling/log"

if not os.path.isdir(directory_path):
    os.mkdir(directory_path)
if not os.path.exists(directory_path+"/count_log.txt"):
    f = open(directory_path+"/count_log.txt", "w", encoding='utf8')
    f.write("로그 기록이 시작됩니다.\n")
    f.close()


with open(directory_path + "/count_log.txt", 'a', encoding="utf8") as f:
    import random, datetime
    for i in range(1, 11):
        stamp = str(datetime.datetime.now())
        value = random.random() * 1000000
        log_line = stamp + "\t" + str(value) + "값이 생성되었습니다." + "\n"
        f.write(log_line)