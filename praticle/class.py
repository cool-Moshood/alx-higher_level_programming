#!/bin/python3
class employee:

    riase_amount = 1.05
    no_emp = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        employee.no_emp += 1
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def riase(self):
       self.age = (self.age * self.riase_amount)
    @classmethod
    def change_age(cls, amount):
        cls.riase_amount = amount

emp_1 = employee("moshood", "age", 25)
emp_2 = employee("olubodun", "yusuf", 23)
emp_3 = employee("olubodun", "yusuf", 23)
emp_4 = employee("olubodun", "yusuf", 23)


employee.change_age(1.09)
emp_2.riase()
print(emp_2.age)
print(emp_1.__dict__)
print(hex(id(employee)))

# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.age)
# print(emp_1.fullname())
# print(emp_2.fullname())
# print(emp_2.age)
# emp_2.riase()
# print(emp_2.age)
# emp_2.riase_amount = 1.08
# emp_2.riase()
# print(emp_2.age)
# print(emp_1.__dict__)
# print(emp_1.riase_amount)
# print(emp_2.__dict__)
print(employee.no_emp)