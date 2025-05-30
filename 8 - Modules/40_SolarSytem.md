# 🌌 The `from` and `as` Keywords - Python Course Notes

## 🧲 `from` Keyword
- Used to import **specific parts** of a module.

### Syntax:
```python
from module_name import object_name
```

### Example:
```python
from random import sample

famous_houses = ['🐺 Stark', '🐉 Targaryen', '🦌 Baratheon', '🦑 Greyjoy', '🦁 Lannister']
example = sample(famous_houses, 2)
print(f'Example: {example}')
```

- We can import multiple items:
```python
from random import choice, sample
```
- `choice()` returns a single random item from a list.

---

## ✍️ `as` Keyword (Aliasing)
- Used to **rename a module or function** for convenience.

### Example:
```python
import random as rd
```
- Now we can use `rd.choice()` instead of `random.choice()`.

### Combining `from` and `as`:
```python
from random import sample as samp
example = samp(['Stark', 'Targaryen', 'Baratheon', 'Greyjoy', 'Lannister'], 2)
print('Example: ' + example[0] + ' ' + example[1])
```

---

## 🪐 Project: `solar_system.py`

### Objective:
Calculate the surface area of a randomly chosen planet.

### Steps:
1. Create a file `solar_system.py`
2. Import:
```python
from math import pi
from random import choice as ch
```
3. Define planets:
```python
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Saturn']
```
4. Select a random planet:
```python
random_planet = ch(planets)
```
Complete Code
```python
# Write code below 💖
from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet=ch(planets)

if random_planet == "Mercury":
  area=4*pi*(2440**2)
  print(random_planet, "'s area is ", area, "km")
elif random_planet == "Venus":
  area=4*pi*(6052**2)
  print(random_planet, "'s area is ", area, "km")
elif random_planet == "Earth":
  area=4*pi*(6371**2)
  print(random_planet, "'s area is ", area, "km")
elif random_planet == "Mars":
  area=4*pi*(3390**2)
  print(random_planet, "'s area is ", area, "km")
elif random_planet == "Saturn":
  area=4*pi*(58232**2)
  print(random_planet, "'s area is ", area, "km")
else:
  print('Oops! An error occurred')
```

### 🔍 Bonus Tip:
- Use `round()` to make the result more readable.
