#!/usr/bin/python3
class Employee:
    """this her lists of the company employee
    """

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@gmail.com"
        self.fullname = first + " " + last

    # def fullname(self):
    #     return "{} {}".format(self.first, self.last)

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)


emp_1 = Employee("john", "snow", 50000)
emp_2 = Employee("jack", "barrow", 65000)

print(emp_1 + emp_2)
print(len(emp_2))

# print(emp_1.__repr__())
# print(emp_2.__str__())
