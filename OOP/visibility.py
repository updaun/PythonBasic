class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.__items = []

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")

        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.__items)
    
    @property
    def items(self):
        # 보통 deepcopy를 해서 반환해준다.
        return self.__items

my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())
print(my_inventory)

# 접근 불가(맹글링)
# print(my_inventory.__items)
# my_inventory.__items.append("abc")

# after decorator
print(my_inventory.items.append("xxx"))
print(my_inventory.items)