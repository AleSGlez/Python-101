# ⏳ Countdown - Python Course Notes

## 📁 Creating Your Own Module
- Any `.py` file can be a module.
- Example: If you have a file `calculator.py` with math functions, you can use them in `main.py`:

```python
import calculator
calculator.add(3, 4)        # 7
calculator.subtract(3, 4)   # -1
calculator.multiply(3, 4)   # 12
calculator.divide(3, 4)     # 0.75
calculator.exp(3, 4)        # 81
```
- Modules must be in the **same folder** to import correctly.

---

## 🕰️ `datetime` Module
- Built-in module for working with dates and times.
- Contains a `date` object with `.year`, `.month`, `.day` properties.

### Create a date:
```python
import datetime
release_date = datetime.date(1991, 2, 20)
print(release_date)  # Output: 1991-02-20
print(release_date.year)  # Output: 1991
```

### Get today’s date:
```python
today = datetime.date.today()
```

You can subtract date objects to find the difference:
```python
time_difference = date1 - date2
```

---

## 🎉 Birthday Countdown Project

### Step 1: `bday_messages.py`
- Create a list of birthday messages:
```python
import random

bday_messages = [
    'Hope you have a very Happy Birthday! 🎈',
    'It\'s your special day – get out there and celebrate! 🎉',
    'You were born and the world got better – everybody wins! 🥳',
    'Have lots of fun on your special day! 🎂',
    'Another year of you going around the sun! 🌞'
]

random_message = random.choice(bday_messages)
```

### Step 2: `main.py`
```python
# Countdown 🎂
# Codédex

import datetime, bday_messages

today = datetime.date.today()

my_next_birthday = datetime.date(2023, 4, 5)

days_away = my_next_birthday - today

if my_next_birthday == today:
  print(bday_messages.random_message)
else:
  print(f'My next birthday is {days_away.days} days away!')
```

---

## 🔄 Bonus Ideas
- Calculate how many days have passed since a special date:
```python
past_event = datetime.date(2020, 3, 1)
days_since = today - past_event
print(f"It\'s been {days_since.days} days since the event.")
```
- You can calculate approximate years or months by dividing days:
```python
years = days_since.days // 365
months = days_since.days // 30
