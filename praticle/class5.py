#!/bin/python3
class employee:

    riase_amount = 1.06

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.email = first + "." + last + "@yahoo.com"

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @property
    def riase(self):
       self.age = (self.age * self.riase_amount)

class developer(employee):
    riase_amount = 1.09
    def __init__(self, first, last, age, job):
        super().__init__(first, last, age)
        self.job = job

class mgr:

    def __init__(self, first, last, age, employees=None):
        super().__init__(first, last, age)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emps):
        if emps not in self.employees:
            self.employees.append(emps)

    def remove_emps(self, emps):
        if emps in self.employees:
            self.employees.remove(emps)

    def Print_emps(self):
        for emps in self.employees:
            print("-->", emps.fullname)





emp_1 = developer("moshood", "age", 25, "CTO")
emp_2 = developer("olubodun", "yusuf", 23, "CFO")

mg_1 = mgr("john", "bond", 50, [emp_1])

print(mg_1.email)

mg_1.add_emps(emp_2)
mg_1.Print_emps


# emp_1.riase
# print(emp_1.age)



if a == "id":
                    if b is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = b
                elif a == "width":
                    self.width = a
                elif a == "height":
                    self.height = a
                elif a == "x":
                    self.x = a
                elif a == "y":
                    self.y = a
