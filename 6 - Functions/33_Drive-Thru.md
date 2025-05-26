# 🚗 Drive-Thru and Function Mastery

You've made it to the end of the functions chapter! Here's what you've learned:

- ✅ The **D.R.Y.** (Don't Repeat Yourself) principle
- 🧩 Built-in functions like `print()` and `input()`
- 🛠️ How to **define and call functions**
- 📥 Using **parameters and arguments**
- 🎁 Sending back values using **`return`**
- 🧠 Understanding **scope** (local vs global)

### 🔧 Function Skeleton:
```python
def function_name(parameter1, parameter2):
    # The code inside
    return value
```

---

## 🛒 Drive-Thru Program (`drive_thru.py`)
Create a simple menu and take an order based on item number input from the user.

```python
# Define Welcome menu
def welcome():
  print("🍔 Welcome to FastBite Drive-Thru!")
  print("Here's our menu:")
  print("#1 - 🍔 Cheeseburger")
  print("#2 - 🌭 Hot Dog")
  print("#3 - 🍟 Fries")
  print("#4 - 🥤 Soda")
  print("#5 - 🍦 Ice Cream")
  print("#6 - 🍪 Cookie")
  print("#7 - 🧇 Waffle")
  return 

#Define get_item() function that takes in one parameter
def get_item(a):
  food=["🍔 Cheeseburger","🌭 Hot Dog","🍟 Fries","🥤 Soda","🍦 Ice Cream","🍪 Cookie","🧇 Waffle"]
  return food[a-1]

# Main program
welcome()
choice = int(input("Enter the number of your item: "))
print("You ordered:", get_item(choice))
```

### 💻 Example Output
```
🍔 Welcome to FastBite Drive-Thru!
Here's our menu:
#1 - 🍔 Cheeseburger
#2 - 🌭 Hot Dog
#3 - 🍟 Fries
#4 - 🥤 Soda
#5 - 🍦 Ice Cream
#6 - 🍪 Cookie
#7 - 🧇 Waffle
Enter the number of your item: 7
You ordered: 🧇 Waffle
```

![CODEDEX (11)](https://github.com/user-attachments/assets/236708b7-6f80-41e8-8d8d-567857e0c735)
