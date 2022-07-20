"""
https://www.programiz.com/python-programming/user-defined-exception

When we are developing a large Python program,
it is a good practice to place all the user-defined exceptions
that our program raises in a separate file.
Many standard modules do this.
They define their exceptions separately as exceptions.py or errors.py
"""


def input_int(message: str) -> int:
    while True:
        try:
            number = int(input(message))
            break
        except ValueError as ve:
            print(ve)
    return number


class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.
    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """
    def __init__(
        self,
        salary: float,
        message: str = "Salary is not in (5000, 15000) range"
    ) -> None:
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.salary} -> {self.message}'


if __name__ == '__main__':
    salary = input_int('Enter salary amount: ')
    if not 5000 < salary < 15000:
        raise SalaryNotInRangeError(salary)





