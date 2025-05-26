# 🏦 Bank Accounts and Instance Methods

## 📘 What Are Instance Methods?
Instance methods are functions defined inside a class that operate on specific objects created from that class.

We’ve used methods like `.append()`, `.remove()`, and `.insert()` with lists — these are built-in instance methods. Now we’re defining our own.

### Syntax Reminder:
```python
class Student:
    def __init__(self, name, year, enrolled, gpa):
        self.name = name
        self.year = year
        self.enrolled = enrolled
        self.gpa = gpa

    def display_info(self):
        print("The student " + self.name + "'s GPA is " + str(self.gpa) + "!")
```

- Like `__init__()`, all instance methods must include `self` as their first parameter.
- `self` refers to the specific object that is calling the method.

```python
mitsuha = Student("宮水三葉", 11, False, 4.0)
taki = Student("立花瀧", 11, True, 3.8)

mitsuha.display_info()  # self refers to mitsuha
taki.display_info()     # self refers to taki
```

📌 **Important:** Like regular functions, **defining a method doesn't run it**. You must call the method explicitly using the object.

---

## 🛒 Bank Account Program (`bank_accounts.py`)
Define a class to simulate basic bank operations:

```python
# Write code below 💖

class BankAccount:
  def __init__(self,first_name, last_name, account_id,account_type,pin,balance):
    self.first_name=first_name
    self.last_name=last_name
    self.account_id=account_id
    self.account_type=account_type
    self.pin=pin
    self.balance=balance

  def deposit(self, amount):
      self.balance += amount
      return self.balance

  def withdraw(self,amount):
    self.balance -= amount
    return self.balance
  
  def display_balance(self):
    print("Current balance:", self.balance)
  
mine=BankAccount('Alex','Glez','0001','Checking Account', 1234, 100)
print(mine)

print(mine.deposit(96))   #Deposit $96
print(mine.withdraw(25))  #Withdraw $25
mine.display_balance()    # Print balance

```

### 💻 Example Output
```
196
171
Current balance: 171
```

![CODEDEX (1)](https://github.com/user-attachments/assets/cf00b754-3ac0-40a0-8f48-61b69b36decc)
