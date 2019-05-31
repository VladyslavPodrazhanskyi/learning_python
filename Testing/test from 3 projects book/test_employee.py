import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee("Vladyslav", "Podrazhanskyi", 35000)

    def test_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 40000)

    def test_customs_raise(self):
        customs_raise = 2500
        self.my_employee.give_raise(customs_raise)
        self.assertEqual(self.my_employee.salary, 37500)



unittest.main()

# class Employee:
#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary
#     def give_raise(self, raise=5000):
#         self.salary += raise

        