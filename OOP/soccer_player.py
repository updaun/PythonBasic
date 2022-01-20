class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" %\
                (self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):
        return "Hello, My name is %s. I play in %s in center and My back number is %d"%\
            (self.name, self.position, self.back_number)

    def __add__(self, other):
        return self.name + other.name

jinhyun = SoccerPlayer("Jinhyun", "MF", 10)
# __str__
print(jinhyun)

park = SoccerPlayer("park", "WF", 13)

# __add__
print(jinhyun + park)


# change_back_number
jinhyun.change_back_number(11)
print(jinhyun)

# direct change
jinhyun.back_number = 20
print(jinhyun)