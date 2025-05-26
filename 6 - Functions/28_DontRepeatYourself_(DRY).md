# 🧩 D.R.Y. Principle and Functions in Python

## 🔁 Don't Repeat Yourself (D.R.Y.)
As programs grow, repeating code becomes a problem. The **D.R.Y. principle** encourages writing clean, maintainable code by reducing repetition.

### 🛠️ Functions to the Rescue
A **function** is a reusable block of code that performs a specific task. Instead of copying code, define it once and call it when needed:
```python
def greet():
    print("Hello, world!")

greet()  # Call the function
```

Functions make your code:
- Cleaner ✅
- Easier to update 🔄
- More organized 📚

---

## ⚙️ Built-in Functions
Python includes **68 built-in functions**. You’ve used several already without realizing it!

### Examples:
- `print()` – Displays text or variables on the screen
- `input()` – Gets input from the user
- `len()` – Returns the number of items in a list, string, etc.
- `type()` – Returns the data type of a value

You don’t need to know how they’re implemented, just how to use them — like driving a car without knowing the engine!

---

## 🛒 DRY Program (`dry.py`)
Create a program that demonstrates built-in functions:

```python
# print() – Displays output
print("Welcome to the D.R.Y. lesson!")

# len() – Returns the number of characters in a string
message = "Stay DRY!"
print(len(message))

# input() – Gets user input
name = input("What's your name? ")
print("Hi, " + name)

# type() – Shows the data type of a variable
print(type(name))

# bin() – NEW! Converts an integer to a binary string
print(bin(13))
```

### 💻 Example Output
```
Welcome to the D.R.Y. lesson!
8
What's your name? Alex
Hi, Alex
<class 'str'>
0b1101
```
