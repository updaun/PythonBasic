class Person(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return "저의 이름은 {0} 입니다. 나이는 {1} 입니다.".format(
            self.name, self.age
        )

class Korean(Person):
    pass

first_korean = Korean("daun", 29)
print(first_korean)


class JobSeeker:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print("저의 이름은", self.name, "입니다. 제 나이는 ", str(self.age), "입니다.")

    def __str__(self) -> str:
        return "저의 이름은", self.name, "입니다. 제 나이는 ", str(self.age), "입니다."


class Employee(JobSeeker): # 부모 클래스 상속
    def __init__(self, name, age, gender, salary, hire_date) -> None:
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date

    def do_work(self):
        print("열일합니다.")

    def about_me(self):
        super().about_me()
        print("제 급여는 ", self.salary, "원이고, 제 입사일은 ", self.hire_date,"입니다.")

first_jobseeker = JobSeeker("John", 34, "Male")
first_jobseeker.about_me()

first_employee = Employee("Daeho", 34, "Male", 3000000, "2020/04/01")
first_employee.about_me()