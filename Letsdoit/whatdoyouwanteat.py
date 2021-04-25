import random
import time

# for x in range(30):
#     print(random.choice(["된장찌개", "피자", "제육볶음", "치킨", "떡볶이", "라면"]))

# lunch = random.choice(["된장찌개", "피자", "제육볶음"])

# dinner = random.choice(["김밥", "쫄면", "돈까스"])

# Dictionary
# information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
# foods = ["된장찌개", "피자", "제육볶음"]
# print(information)
# print(type(information))
# print(information.get("취미"))
# information["특기"] = "피아노"
# information["사는곳"] = "서울"
# del information["좋아하는 음식"]
# print(information)
# print(len(information))
# information.clear()
# print(information)
# print(foods[1])
# foods.append("김밥")
# print(foods)

# for x in range(30):
#     print(x)

# foods = ["된장찌개","피자","제육볶음"]

# for x in foods:
#     print(x)

# information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
# for x,y in information.items():
#     print(x)
#     print(y)

# foods = ["된장찌개","피자","제육볶음"]

# foods_set1 = set(foods)
# foods_set2 = set(["된장찌개","피자","제육볶음"])

# print(foods_set1)
# print(type(foods_set1))
# print(foods_set2)
# print(type(foods_set2))

# foods = ["된장찌개","피자","제육볶음","된장찌개"]
# foods_set = set(foods)

# print(foods)
# print(foods_set)

# menu1 = set(["된장찌개","피자","제육볶음"])
# menu2 = set(["된장찌개","떡국","김밥"])

# menu3 = menu1 | menu2 # 합집합 : 파이프심볼(|) 사용
# menu3 = menu1 & menu2 # 교집합 : & 사용
# menu3 = menu1 - menu2 # 차집합 : - 사용

# print(menu3) 

# food = random.choice(["된장찌개","피자","제육볶음"])
# if food == "제육볶음":
#     print(food,"곱빼기 주세요")
# else:
#     print(food,"그냥 주세요")
# print("종료")

# set_lunch = set(["된장찌개","피자","제육볶음","짜장면"])

# item = "짜장면"

# print(set_lunch - set([item]))
# set_lunch = set_lunch - set([item])
# print(set_lunch)

# set_dinner = set(["된장찌개","피자","제육볶음","짜장면"])

# food = "짜장면"
# set_dinner = set_dinner - set([food])
# print(set_dinner)

lunch = ["된장찌개","피자","제육볶음","짜장면"]

while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : ")
    if item == "q":
        break
    else:
        lunch.append(item)
print(lunch)
set_lunch = set(lunch)

while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요 : ")
    if item == "q":
        break
    else:
        set_lunch = set_lunch - set([item])

print(set_lunch, "중에서 선택합니다.")
# print("5")
# time.sleep(1)
# print("4")
# time.sleep(1)
# print("3")
# time.sleep(1)
# print("2")
# time.sleep(1)
# print("1")
# time.sleep(1)
for i in range(5):
    number = 5 - i
    print(number)
    time.sleep(1)

print("오늘의 점심은 !! ", random.choice(list(set_lunch)), "입니다!")