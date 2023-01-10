#!/usr/bin/python3
class Employee:
    """this her lists of the company employee
    """

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split( )
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("NAME HAS BEEN DELETED!")
        self.first = None
        self.last = None





emp_1 = Employee("john", "snow", 50000)
emp_2 = Employee("jack", "barrow", 65000)

emp_1.fullname = "joy peace"
print(emp_1.fullname)
print(emp_1.email)
del emp_1.fullname
print(emp_1.fullname)
print(emp_1.email)