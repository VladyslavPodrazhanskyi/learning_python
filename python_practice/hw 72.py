"""
Task 7_2
Create classes Employee, SalesPerson, Manager and Company with predefined functionality.

Create basic class Employee and declare following content:
• Attributes – `name` (str), `salary` and `bonus` (int), set with property decorator
• Constructor - parameters `name` and `salary`
• Method `bonus` - sets bonuses to salary, amount of which is delegated as `bonus`
• Method `to_pay` - returns the value of summarized salary and bonus.

Create class SalesPerson as class Employee inheritor and declare within it:
• Constructor with parameters: `name`, `salary`, `percent` – percent of plan performance (int, without the % symbol),
 first two of which are passed from basic class constructor
• Redefine method of parent class `bonus` in the following way: if the sales person completed the plan more than 100%,
their bonus is doubled (is multiplied by 2), and if more than 200% - bonus is tripled (is multiplied by 3)

Create class Manager as Employee class inheritor, and declare within it:
• Constructor with parameters: `name`, `salary` and `client_number` (int, number of served clients), first two of which
are passed to basic class constructor.
• Redefine method of parent class `bonus` in the following way: if the manager served over 100 clients, their bonus is
increased by 500, and if more than 150 clients – by 1000.

Create class Company and declare within it:
• Constructor with parameters: `employees` – list of company`s employees (made up of Employee/SalesPerson/Manager classes
 instances) with arbitrary length `n`
• Method `give_everybody_bonus` with parameter company_bonus (int) that sets the amount of basic bonus for each employee.
• Method `total_to_pay` that returns total amount of salary of all employees including awarded bonus
• Method `name_max_salary` that returns name of the employee, who received maximum salary including bonus.

Note:
Class attributes and methods should bear exactly the same names as those given in task description
Methods should return only target values, without detailed explanation within `return`
"""


class Employee:
    def __init__(self, name: str, salary: int):
        self.__name = name
        self.__salary = salary
        self.__bonus = 0

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, value):
        self.__bonus = value

    def to_pay(self):
        return self.__salary + self.__bonus


class SalesPerson(Employee):
    def __init__(self, name, salary, percent):
        super().__init__(name, salary)
        self.__percent = percent

    @Employee.bonus.setter
    def bonus(self, value):
        if self.__percent > 200:
            bonus_mult = 3
        elif self.__percent > 100:
            bonus_mult = 2
        else:
            bonus_mult = 1
        super(SalesPerson, type(self)).bonus.fset(self, value * bonus_mult)


class Manager(Employee):
    def __init__(self, name, salary, client_number):
        super().__init__(name, salary)
        self.__client_number = client_number

    @Employee.bonus.setter
    def bonus(self, value):
        if self.__client_number > 150:
            bonus_add = 1000
        elif self.__client_number > 100:
            bonus_add = 500
        else:
            bonus_add = 0
        super(Manager, type(self)).bonus.fset(self, value + bonus_add)


class Company:
    def __init__(self, employees, n=None):
        self.__employees = employees
        self.__n = n

    @property
    def employees(self):
        return self.__employees

    @property
    def n(self):
        return self.__n

    def give_everybody_bonus(self, company_bonus: int):
        for employee in self.__employees:
            employee.bonus = company_bonus

    def total_to_pay(self):
        return sum(map(lambda x: x.to_pay(), self.__employees))

    def name_max_salary(self):
        # max_pay_employee = self.__employees[0]
        # for employee in self.__employees[1:]:
        #     if employee.to_pay() > max_pay_employee.to_pay():
        #         max_pay_employee = employee
        # return max_pay_employee.name
        list_to_pay = list(map(lambda x: x.to_pay(), self.__employees))
        max_index = list_to_pay.index(max(list_to_pay))
        return self.__employees[max_index].name


e1 = Employee('Serge', 6000)
e2 = Employee('Alex', 7000)

s1 = SalesPerson('Max', 10000, 120)
s2 = SalesPerson('Olga', 8000, 180)

m1 = Manager("Victor", 15000, 300)
m2 = Manager("Oleg", 11000, 100)

company = Company([e1, e2, s1, s2, m1, m2])

# print(company.total_to_pay())
# company.give_everybody_bonus(1000)
# print(company.total_to_pay())
# print(company.name_max_salary())
#
print(" -> ".join((map(lambda x: x.__name__, Manager.mro()))))
print(*(map(lambda x: x.__name__, Manager.mro())), sep=' -> ')

print(*[c.__name__ for c in Manager.mro()], sep=" -> ")
print(" -> ".join([c.__name__ for c in Manager.mro()]))