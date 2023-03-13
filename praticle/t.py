#!/usr/bin/python3

class employee:
    raise_amt = 1.09
    no_emp = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        employee.no_emp += 1
        self.email = first + "." + last + "@gmail.com"
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @property
    def new_age(self):
        return "the new age is {:2f}".format(self.age * self.raise_amt)

    @property
    def update_age(self):
        self.age = self.age * self.raise_amt

    @classmethod
    def change_amt(cls, amt):
        cls.raise_amt = amt

    @classmethod
    def change_name(cls, string):
        first, last, age = string.split("-")
        return cls(first, last, age)

class developer(employee):

    def __init__(self, first, last, age, height):
        super().__init__(first, last, age)
        self.height = height

class mgr(developer):
    def __init__(self, first, last, age, employees = None):
        super().__init__(first, last, age, height)

        if self.employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emps(self, emps):
        if emps not in self.employees:
            self.employees.append(emps)

    def remove_emps(self, emps):
        if emps in self.employees:
            self.employees.remove(emps)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emps.fullname)







dev_1 = developer("mopelola", "oluwa", 23, "5.7ft")

print(dev_1.height)

mgr_1 = mgr("john", "cook", 45, 5.3, [dev_1])

print(mgr_1.email)




dev_1 = employee("mopelola", "rodiat", 29)
dev_2 = employee("mopelola", "dancing", 24)
dev_3 = employee("mopelola", "pele", 22)
dev_4 = "halimat-igando-23"

# print(dev_1.email)
# print(dev_1.first)
# print(dev_1.last)
# print(dev_1.fullname)
# print(dev_1.new_age)
# print(employee.no_emp)
# dev_2.update_age
# print(round(dev_2.age, 2))
# print(dev_2.__dict__)
# print(hex(id(employee)))
# employee.change_amt = 1.05
# dev_2.update_age
# print(round(dev_2.age, 2))
# dev_5 = employee.change_name(dev_4)
# print(dev_5.first)
# print(dev_5.last)
# print(dev_5.age)
