class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first,
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    def __repr__(self):
        return f"Employee({self.first} {self.last} {self.pay})"

    def __str__(self):
        return f"{self.fullname} {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

""" emp_1  = Employee('sam', 'tan', 200000)
emp_2 = Employee('ram', 'tan', 500000) """

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



    

emp_1  = Employee('sam', 'tan', 200000)
emp_2 = Employee('ram', 'tan', 500000)

""" print(dev_1.prog_lang)
print(dev_2.prog_lang) """


""" import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))


man_1 = Manager('Sam', 'Doe', 10000, [dev_1])

print(isinstance(man_1, Manager))
print(issubclass(Manager, Employee)) """

del emp_1.fullname
#print(str(emp_1))

print(emp_1.fullname)