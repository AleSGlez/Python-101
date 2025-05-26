# 🔢 Calculator and Return Values in Python

## 🎁 Return Values
Functions in Python can send values back using the `return` keyword. This makes your functions **more powerful and flexible**.

### Without Return:
```python
def greet():
    print("Hello!")
```
You can only see output when it's printed.

### With Return:
```python
def add(x, y):
    return x + y

total = add(4.99, 9.99)
print(total)  # 14.98
```
The value is **returned** and can be stored or reused anywhere in your code.

💡 When Python reaches a `return` statement, it exits the function and sends back the value.

---

## 🖨️ Print vs. Return
- Use `print()` to display info to the user.
- Use `return` to send values between parts of your program.

---

## 🛒 Calculator Program (`calculator.py`)
Create a Python program that defines and uses 5 functions:

```python
def add(x,y):
  ans=x+y
  return ans

def subtract(x,y):
  ans=x-y
  return ans

def multiply(x,y):
  ans=x*y
  return ans

def divide(x,y):
  ans=x/y
  return ans

def exp(x,y):
  ans=x**y
  return ans

print(add(1,5))
print(subtract(10,5))
print(multiply(85,5))
print(divide(81,9))
print(exp(2,5))
```

### 💻 Example Output
```
6
5
425
9.0
32
```

✅ Each function returns the result of the operation so it can be reused or displayed.

![CODEDEX (9)](https://github.com/user-attachments/assets/bd126c21-299b-46bb-9922-7cf97e74a923)

