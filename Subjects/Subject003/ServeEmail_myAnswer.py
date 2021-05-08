# 1) 이름, 전화번호, e-mail을 입력받아 dict에 저장하고
# 이름에 ‘end’가 입력되면 전체 dict 내용을 출력하며,
# 이어서 이름을 입력 받아 입력받은 이름으로 검색해서 찾으면 이름, 전화번호, e-mail을 출력하고,
# 찾지 못하면  error 메시지를 출력하며 이름이 ‘end’이면 종료하는 파이썬 스크립트

# info_all_list = []
# info_dict = {"이름":"","전화번호":"","e-mail":""}

# while True: 
#     info_dict["이름"] = input("이름을 입력하세요 : ")
#     if info_dict["이름"] == "end":
#         break
#     info_dict["전화번호"] = input("전화번호를 입력하세요 : ")
#     info_dict["e-mail"] = input("e-mail을 입력하세요 : ")

#     info_all_list.append(info_dict)

# print(info_all_list)

# search_name = input("정보를 검색할 이름을 입력하세요 : ")

# for i in info_all_list:
#     if i.get("이름") == search_name:
#         print(f'이름 {i["이름"]} \n전화번호 {i["전화번호"]} \nemail {i["e-mail"]}')

info_dict = {}

while True:
    name = input("이름을 입력하세요 : ")
    if name == 'end':
        break
    tel = input("전화번호를 입력하세요 : ")
    email = input("e-mail을 입력하세요 : ")

    info_dict[name] = [tel, email]

print(info_dict)

search_name = input("정보를 검색할 이름을 입력하세요 : ")

key = info_dict.keys()
if (search_name in list(key)) == False:
    print(info_dict.get(search_name, "Error : 정보를 찾을 수 없습니다."))

for k,v in info_dict.items():
    # print(k,v)
    if k == search_name:
        print(f'이름 :{k} \n전화번호 : {v[0]} \nemail : {v[1]}')

