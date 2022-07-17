# Types and classes
# So far, we’ve only seen examples of pre-existing types like the int or float builtins,
# or generic types from collections.abc and typing, such as Iterable.
# However, these aren’t the only types you can use: in fact, you can use any Python class as a type!
#
# For example, suppose you’ve defined a custom class representing a bank account:

class BankAccount:
    # Note: It is ok to omit type hints for the "self" parameter.
    # Mypy will infer the correct type.

    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        # Note: Mypy will infer the correct types of your fields
        # based on the types of the parameters.
        self.account_name = account_name
        self.balance = initial_balance

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.balance -= amount

    def overdrawn(self) -> bool:
        return self.balance < 0


# You can declare that a function will accept any instance
# of your class by simply annotating the parameters with BankAccount:

def transfer(src: BankAccount, dst: BankAccount, amount: int) -> None:
    src.withdraw(amount)
    dst.deposit(amount)


account_1 = BankAccount('Alice', 400)
account_2 = BankAccount('Bob', 200)
transfer(account_1, account_2, 50)


# In fact, the transfer function we wrote above can accept more
# then just instances of BankAccount: it can also accept any instance of a subclass of BankAccount.
# For example, suppose you write a new class that looks like this:

class AuditedBankAccount(BankAccount):
    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        super().__init__(account_name, initial_balance)
        self.audit_log: list[str] = []

    def deposit(self, amount: int) -> None:
        self.audit_log.append(f"Deposited {amount}")
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.audit_log.append(f"Withdrew {amount}")
        self.balance -= amount


# Since AuditedBankAccount is a subclass of BankAccount,
# we can directly pass in instances of it into our transfer function:

audited = AuditedBankAccount('Charlie', 300)
transfer(account_1, audited, 100)  # Type checks!
