
# product_name = input("품목명을 입력하세요.(end 입력시 종료) : ")

# while product_name != 'end':
#     product_name = input("품목명을 입력하세요.(end 입력시 종료) : ")

product_dict = {}
sales_list = []

print("[ 품목 정보 입력 ]")
while True:
    product_name = input("품목명 : ")

    if product_name == 'end':
        break

    product_dict[product_name] = []
     
    
    product_price = input("판매단가 : ")

    if product_price == 'end':
        product_price = 0
        break

    product_dict[product_name].append(int(product_price))
    print()

print(product_dict)

print("[ 판매 정보 입력 ]")
while True:
    product_name = input("품목명 : ")

    if product_name == 'end':
        break
    if product_name not in product_dict.keys():
        print("error : 등록되지 않은 품목입니다. 다시 입력하세요.")

    num_sales = input("판매수량 : ")

    if num_sales == 'end':
        break

    product_dict[product_name].append(int(num_sales))

    sales = product_dict[product_name][0] * product_dict[product_name][1]
    product_dict[product_name].append(sales)
    print()
print(product_dict)