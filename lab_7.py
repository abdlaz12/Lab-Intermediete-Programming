class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        if (not isinstance(numerator, int) or not isinstance(denominator, int)):
            raise TypeError("The numerator and denominator must be integers.")

        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        else:
            if (numerator < 0 and denominator >= 0) or (numerator >= 0 and denominator < 0):
                sign = -1
            else:
                sign = 1
            a = abs(numerator)
            b = abs(denominator)
            while a % b != 0:
                tempA = a
                tempB = b
                a = tempB
                b = tempA % tempB
            self._numerator = abs(numerator) // b * sign
            self._denominator = abs(denominator) // b

    def __str__(self):
        if self._denominator == 1:
            return str(self._numerator)
        else:
            return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"

    def __add__(self, other):
        if isinstance(other, Fraction):
            num = self._numerator * other._denominator + other._numerator * self._denominator
            den = self._denominator * other._denominator
            return Fraction(num, den)
        elif isinstance(other, int):
            return self + Fraction(other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            num = self._numerator * other._denominator - other._numerator * self._denominator
            den = self._denominator * other._denominator
            return Fraction(num, den)
        elif isinstance(other, int):
            return self - Fraction(other)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            num = self._numerator * other._numerator
            den = self._denominator * other._denominator
            return Fraction(num, den)
        elif isinstance(other, int):
            return self * Fraction(other)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other._numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            num = self._numerator * other._denominator
            den = self._denominator * other._numerator
            return Fraction(num, den)
        elif isinstance(other, int):
            return self / Fraction(other)
        else:
            return NotImplemented

    def __pow__(self, power):
        if not isinstance(power, int):
            return NotImplemented
        if power >= 0:
            num = self._numerator ** power
            den = self._denominator ** power
        else:
            num = self._denominator ** abs(power)
            den = self._numerator ** abs(power)
        return Fraction(num, den)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self._numerator == other._numerator and self._denominator == other._denominator
        elif isinstance(other, int):
            return self == Fraction(other)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self._numerator * other._denominator < other._numerator * self._denominator
        elif isinstance(other, int):
            return self < Fraction(other)
        else:
            return NotImplemented

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

    def __neg__(self):
        return Fraction(-self._numerator, self._denominator)

    def __pos__(self):
        return Fraction(self._numerator, self._denominator)

    def __abs__(self):
        return Fraction(abs(self._numerator), self._denominator)

    def __int__(self):
        return self._numerator // self._denominator

    def __float__(self):
        return self._numerator / self._denominator

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return -self + other

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Fraction(other) / self
        else:
            return NotImplemented

    def __iadd__(self, other):
        result = self + other
        self._numerator, self._denominator = result._numerator, result._denominator
        return self

    def __isub__(self, other):
        result = self - other
        self._numerator, self._denominator = result._numerator, result._denominator
        return self

    def __imul__(self, other):
        result = self * other
        self._numerator, self._denominator = result._numerator, result._denominator
        return self

    def __itruediv__(self, other):
        result = self / other
        self._numerator, self._denominator = result._numerator, result._denominator
        return self

    def __ipow__(self, other):
        result = self ** other
        self._numerator, self._denominator = result._numerator, result._denominator
        return self
    
# Membuat instance Fraction
f1 = Fraction(3, 4)
f2 = Fraction(2, 5)

# Menampilkan instance Fraction
print(f"f1: {f1}")  # Output: f1: 3/4
print(f"f2: {f2}")  # Output: f2: 2/5

# Operasi penjumlahan
f3 = f1 + f2
print(f"f1 + f2: {f3}")  # Output: f1 + f2: 23/20

# Operasi pengurangan
f4 = f1 - f2
print(f"f1 - f2: {f4}")  # Output: f1 - f2: 7/20

# Operasi perkalian
f5 = f1 * f2
print(f"f1 * f2: {f5}")  # Output: f1 * f2: 3/10

# Operasi pembagian
f6 = f1 / f2
print(f"f1 / f2: {f6}")  # Output: f1 / f2: 15/8

# Operasi pangkat
f7 = f1 ** 2
print(f"f1 ** 2: {f7}")  # Output: f1 ** 2: 9/16

# Operasi pembanding
print(f"f1 == f2: {f1 == f2}")  # Output: f1 == f2: False
print(f"f1 < f2: {f1 < f2}")    # Output: f1 < f2: False
print(f"f1 <= f2: {f1 <= f2}")  # Output: f1 <= f2: False
print(f"f1 > f2: {f1 > f2}")    # Output: f1 > f2: True
print(f"f1 >= f2: {f1 >= f2}")  # Output: f1 >= f2: True

# Operasi unary
print(f"-f1: {-f1}")  # Output: -f1: -3/4
print(f"+f1: {+f1}")  # Output: +f1: 3/4
print(f"abs(f1): {abs(f1)}")  # Output: abs(f1): 3/4

# Konversi ke tipe lain
print(f"int(f1): {int(f1)}")  # Output: int(f1): 0
print(f"float(f1): {float(f1)}")  # Output: float(f1): 0.75

# Operasi augmented assignment
f1 += f2
print(f"f1 += f2: {f1}")  # Output: f1 += f2: 23/20

f1 -= f2
print(f"f1 -= f2: {f1}")  # Output: f1 -= f2: 3/4

f1 *= f2
print(f"f1 *= f2: {f1}")  # Output: f1 *= f2: 3/10

f1 /= f2
print(f"f1 /= f2: {f1}")  # Output: f1 /= f2: 3/4

f1 **= 2
print(f"f1 **= 2: {f1}")  # Output: f1 **= 2: 9/16

print("                                                                                         ")
print("                                                                                         ")

import random

class BankAccount:
    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance
        self.account_number = self._generate_account_number()

    def _generate_account_number(self):
        return random.randint(10000000, 99999999)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")

    def check_balance(self):
        print(f"Account balance for {self.owner_name}: ${self.balance}")

    def get_account_number(self):
        return self.account_number

    def __str__(self):
        return f"Account {self.account_number} - {self.owner_name}, Balance: ${self.balance}"

# Function to create multiple accounts
def create_accounts(num_accounts):
    accounts = []
    names = ["Alice", "Bob", "Charlie", "Diana", "Evan", "Fiona", "George", "Hannah", "Ian", "Julia"]
    
    for i in range(num_accounts):
        name = random.choice(names)
        initial_balance = random.randint(0, 1000)
        account = BankAccount(name, initial_balance)
        accounts.append(account)
    
    return accounts

# Main program
num_accounts = 5
bank_accounts = create_accounts(num_accounts)

print("Created Accounts:")
for account in bank_accounts:
    print(account)
    print(f"  Account Number: {account.get_account_number()}\n")

# Example operations on the first account
first_account = bank_accounts[0]
first_account.deposit(500)
first_account.withdraw(200)
first_account.check_balance()

print("                                                                                         ")
print("                                                                                         ")

class Family:
    def __init__(self, last_name, parents):
        self.last_name = last_name
        self.parents = parents
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __iter__(self):
        return iter(self.children)

    def __len__(self):
        return len(self.children)

    def __str__(self):
        parent_names = " & ".join(parent.name for parent in self.parents)
        children_names = ", ".join(child.name for child in self.children) if self.children else "No children yet"
        return f"{self.last_name} Family: {parent_names} with children: {children_names}"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

# Example usage
mom = Person("Jane", 35)
dad = Person("John", 38)
smith_family = Family("Smith", [mom, dad])

smith_family.add_child(Person("Alice", 10))
smith_family.add_child(Person("Bob", 8))
smith_family.add_child(Person("Charlie", 6))

print(smith_family)

print("Children:")
for child in smith_family:
    print(f"  - {child}")

print(f"Number of children: {len(smith_family)}")
