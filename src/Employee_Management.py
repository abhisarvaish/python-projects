import datetime


class Employee:
    raise_amount = 1.05
    total_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.total_employees += 1

    def print_data(self):
        return f'{self.first}-{self.last}-{self.pay}'

    def pay_raise(self):
        self.pay *= self.raise_amount
        return self.pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @classmethod
    def format(cls, str_val):
        first, last, pay = str_val.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __mul__(self, other):
        return int(self.pay) * other

    __rmul__ = __mul__


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

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(emp.first, emp.last)


# dev_1 = Developer("Palm","Lower",45667,"Python")
# dev_2 = Developer("Kiran","Pandey",56666,"Java")
# dev_3 = Developer("Kalim","Khan",20000,"Ruby")
# dev_1.pay_raise()
# print(dev_1.prog_lang)

# mgr_1 = Manager("Sudd","Aggarwal",90000,[dev_1,dev_2])
# mgr_1.print_emp()
# mgr_1.add_emp(dev_3)
# mgr_1.print_emp()
# mgr_1.remove_emp(dev_2)
# mgr_1.print_emp()
# mydate = datetime.date(2023, 8, 5)
# print(Employee.is_workday(mydate))

str_value = 'Nathan-Lyon-40000'
#
# emp_1 = Employee ("Rhea", "Paul", 50000)
# emp_2 = Employee("Sasha", "Grey", 1320000)
# print(emp_1.pay)
# print(emp_1.pay_raise())
# print(emp_1.__dict__)
# print(Employee.__dict__)

emp_3 = Employee.format(str_value)

# print(emp_3.__repr__())
# Employee.raise_amount = 4
# print(Employee.total_employees)

# print(3 * emp_3)
# emp_1.raise_amount = 1.20
# print(emp_3.email)
# print(emp_3.first)

# emp_3.fullname = 'Raj Malhotra'
# print(emp_3.fullname)
# print(emp_3.email)
# print(emp_3.first)


# IMP Can instance variable call class methods?
"""A class method is a method that's shared among all objects. To call a class method,
put the class as the first argument. Class methods can be can be called from
instances and from the class itself. All of these use the same method."""


class A:

    def __init__(self, name: str) -> None:
        self.name = name
        print('Init Called')

    @classmethod
    def set_name(cls, name: str):
        return cls(name)

    def display(self):
        print(self.name)


# instance variable a is created with name = Abhi
a = A('Abhi')
# Will display Abhi
a.display()

# Class method is bieng called with a class A as first parameter and 'Ramu' as second parameter
# a new object is created with name = Ramu and will be assigned to 'a'
a = A.set_name('Ramu')

# so this will display 'Ramu'
a.display()

# Now class method 'set_name' is bieng called with instance 'a' as first parameter and 'Pram' as second parameter
# Since class method is available to all, so new object will be created and assigned to 'b' with name 'Pram'
b = a.set_name('Pram')
# This will display 'Pram'
b.display()

# and since 'a' as used to create a new object above, noting will be changes for 'a' and will still hold name as 'Ramu'
a.display()

# Can I access an instance-variable using a @classmethod?
# No. The class method is not given a reference to the instance object so its data is unavailable.
