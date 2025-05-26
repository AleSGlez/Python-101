# 🎰 Slot Machine - Python Course Notes

## 🧩 Modules in Python
- A **module** is any `.py` file containing functions, statements, or class definitions with a common purpose.
- Python includes over **200 built-in modules**.

### Examples:
- `random` – generate random numbers.
- `math` – do mathematical calculations.
- `datetime` – handle dates and times.

Modules are useful because they save us from writing complex functionality from scratch.

---

## 🎲 Using the `random` Module
We revisit the `random` module, especially its `.choices()` method.

```python
import random

dice = [1, 2, 3, 4, 5, 6]
print(random.choices(dice))
```

- `import` lets us use the module.
- `.choices()` picks a random item (or more with `k=`).

```python
print(random.choices(dice, k=3))  # picks 3 random items
```

Note: Items **can repeat** in the returned list.

---

## 📦 Importing Multiple Modules
Two options:

```python
import random
import math
```
Or:
```python
import random, math
```
Both are valid and equivalent.

---

## 🛠️ Final Project: Slot Machine
Create a file named `slot_machine.py`

### Program Requirements:
- Import the `random` module.
- Create a list: 
```python
symbols = ['🍒', '🍇', '🍉', '7️⃣']
```
- Use `random.choices()` to select 3 symbols:
```python
results = random.choices(symbols, k=3)
```
- Print the results separated by pipes:
```python
print(f"{results[0]} | {results[1]} | {results[2]}")
```
- Use conditional logic:
```python
if results[0]=='7️⃣' and results[1]=='7️⃣' and results[2]=='7️⃣':
  print("Jackpot! 💰")
else:
  print("Thanks for playing!")
```
### 💻 Example Output
```
 🍇 | 7️⃣ | 🍉
Thanks for playing!
```

![CODEDEX](https://github.com/user-attachments/assets/3a92fcd3-c56e-42d0-b680-209e30572932)

### 🎯 Bonus Features:
- Wrap everything in a `play()` function.
- Use a `while` loop to let players continue.
- Ask for player input using:
```python
import random

symbols = ['🍒', '🍇', '🍉', '7️⃣']

def play():
    results = random.choices(symbols, k=3)
    print(f"{results[0]} | {results[1]} | {results[2]}")
    
    if results[0] == results[1] == results[2] == '7️⃣':
        print("Jackpot! 💰")
    else:
        print("Thanks for playing!")

while True:
    play()
    play_again = input("Play again? (Y/N): ").strip().upper()
    if play_again != 'Y':
        print("Goodbye! 👋")
        break

```
### 💻 Example Output
```
🍒 | 🍉 | 🍒
Thanks for playing!
Play again? (Y/N): Y
7️⃣ | 🍇 | 🍉
Thanks for playing!
Play again? (Y/N): Y
🍉 | 🍉 | 🍇
Thanks for playing!
```
![CODEDEX (1)](https://github.com/user-attachments/assets/a146db34-182f-47c5-b8ec-62a474f86155)
