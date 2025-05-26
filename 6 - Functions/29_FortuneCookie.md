# 🥠 Fortune Cookie and Defining Functions

## 🧠 What is a Function?
A **function** is a reusable block of code that performs a specific task. Creating a function is a two-step process:

1️⃣ Define it using `def`
2️⃣ Call it using its name and `()`

### Example:
```python
def say_hello():
    print("Howdy! 🤠")
    print("How are you?")

say_hello()  # Call the function
```

Functions help you:
- Avoid repeating code (D.R.Y.)
- Keep your code clean and organized
- Run a block of code multiple times just by calling it

---

## 🛒 Fortune Cookie Program (`fortune_cookie.py`)
Create a Python program that prints random fortunes to the user:

```python
import random

def fortune(): #function definition
  #code inside function = body of the function
  num_fort=random.randint(1,8)
  if num_fort==1:
    print("Don't pursue happiness – create it.")
  elif num_fort==2:
    print("All things are difficult before they are easy.")
  elif num_fort==3:
    print("The early bird gets the worm, but the second mouse gets the cheese.")
  elif num_fort==4:
    print("Someone in your life needs a letter from you.")
  elif num_fort==5:
    print("Don't just think. Act!")
  elif num_fort==6:
    print("Your heart will skip a beat.")
  elif num_fort==7:
    print("The fortune you search for is in another cookie.")
  elif num_fort==8:
    print("Help! I'm being held prisoner in a Chinese bakery!")
  else:
    print('Error: no fortune for you')

print('If/elif/else test')
fortune()
fortune()
```

### 💻 Example Output
```
If/elif/else test
The fortune you search for is in another cookie.
Your heart will skip a beat.
```
![CODEDEX (6)](https://github.com/user-attachments/assets/da741698-1c2c-4d82-a99c-ca2ec51da44e)

🔁 Bonus: Try rewriting the function using a list instead of `if/elif/else`!

```python
import random

#Bonus
def fortune_bonus():
  num_fort=random.randint(1,8)
  fort_quotes=["Don't pursue happiness – create it.","All things are difficult before they are easy.","The early bird gets the worm, but the second mouse gets the cheese.","Someone in your life needs a letter from you.","Don't just think. Act!","Your heart will skip a beat.", "The fortune you search for is in another cookie.","Help! I'm being held prisoner in a Chinese bakery!"]
  print(fort_quotes[num_fort])

print('Bonus Test')
fortune_bonus()
fortune_bonus()
fortune_bonus()
```

### 💻 Example Output
```
Bonus Test
Don't just think. Act!
All things are difficult before they are easy.
All things are difficult before they are easy.
```
![CODEDEX (7)](https://github.com/user-attachments/assets/ca0f4ab3-bda9-4409-bd23-b9569ef211c8)
