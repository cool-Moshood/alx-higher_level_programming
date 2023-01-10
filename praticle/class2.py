#!/bin/python3
class Employee:
    no_emp = 0
    riase_amount = 1.05

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.email = first + "." + last + "@gmail.com"
        Employee.no_emp += 1
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def riase(self):
       self.age = (self.age * self.riase_amount)
    @classmethod
    def change_age(cls, amount):
        cls.riase_amount = amount

    @classmethod
    def change_string(cls, string):
        first, last, age = string.split("-")
        return cls(first, last, age)

    @staticmethod
    def is_workday(day):
        if day == 5 or day == 6:
            return False
        return True

emp_1 = Employee("moshood", "age", 25)
emp_2 = Employee("olubodun", "yusuf", 23)
em_1= "jack-bambam-50"
emp_4 = Employee.is_workday(5)

emp_3 = Employee.change_string(em_1)
print(emp_3.first)
print(emp_3.fullname())
print(emp_3.email)
print(emp_3.age)
print(emp_4)


# print(emp_1.first)
# print(emp_1.fullname())
# print(emp_1.email)
# print(emp_1.age)
# emp_1.riase()
# print(emp_1.age)
# emp_2.change_age(30)
# print(emp_2.riase_amount)
# emp_2.riase()
# print(emp_2.age)