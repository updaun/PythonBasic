# open
f = open("file_handling/test.txt", "r", encoding="utf-8")
contents = f.read()
print(contents)
f.close()

# with 구문 사용시 close로 닫지 않아도 된다.
with open("file_handling/test.txt", "r", encoding="utf-8") as my_file:
    contents = my_file.read()
    print(type(contents), contents)

# readlines
with open("file_handling/test.txt", "r", encoding="utf-8") as my_file:
    contents_list = my_file.readlines()
    print(contents_list)

# readline
with open("file_handling/test.txt", "r", encoding="utf-8") as my_file:
    i = 0
    while True:
        line = my_file.readline()
        if not line:
            break
        print( str(i) + "===" + line.replace("\n",""))
        i += 1