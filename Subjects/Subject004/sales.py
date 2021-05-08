global product_dict
product_dict = {}


def make_product_info():
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
        product_dict[product_name].append(0)
        product_dict[product_name].append(0)
        print()
    print()
    return product_dict


def make_sales_info():
    while True:
        product_name = input("품목명 : ")

        if product_name == 'end':
            break

        if product_name not in product_dict.keys():
            print("error : 등록되지 않은 품목입니다. 다시 입력하세요.\n")
            make_sales_info()
            break

        num_sales = input("판매수량 : ")

        if num_sales == 'end':
            break

        product_dict[product_name][1] += (int(num_sales))

        sales = product_dict[product_name][0] * product_dict[product_name][1]
        product_dict[product_name][2] = sales
        print()
    return product_dict


def main():
    print("[ 품목 정보 입력 ]")
    make_product_info()

    print("[ 판매 정보 입력 ]")
    make_sales_info()
    print('\n'*2)
    print("            판매 일람표            \n")
    print()
    print("품목명   판매단가  판매수량  판매금액")

    for i in product_dict.keys():
        print(
            f'{i}\t{product_dict[i][0]}\t\t{product_dict[i][1]}\t{product_dict[i][2]}')


if __name__ == "__main__":
    main()
