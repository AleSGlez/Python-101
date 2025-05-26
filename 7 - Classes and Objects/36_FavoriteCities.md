# 🏙️ Favorite Cities and the `__init__()` Method

## 📦 What is `__init__()`?
The `__init__()` method lets us **automatically assign values to object attributes** when we create an object. This avoids writing many manual lines like:
```python
obj.name = 'Daniel'
obj.year = 10
```

### Old Way:
```python
class Student:
    name = ''
    year = 0
    gpa = 0.0
    enrolled = False

daniel = Student()
daniel.name = 'Daniel Li'
daniel.year = 10
```

### New Way with `__init__()`:
```python
class Student:
    def __init__(self, name, year, gpa, enrolled):
        self.name = name
        self.year = year
        self.gpa = gpa
        self.enrolled = enrolled

daniel = Student('Daniel Li', 10, 4.0, True)
```
Much cleaner and scalable!

---

## 🛒 Favorite Cities Program (`favorite_cities.py`)
Use `__init__()` to build a `City` class with relevant attributes:

```python
class City:
  def __init__(self, name, country, language,population, landmarks, currency):
    self.name=name
    self.country=country
    self.language=language
    self.population=population
    self.landmarks=landmarks
    self.currency=currency
  
mexico=City('Mexico City','Mexico','Spanish',22752400,['Diana', 'Angel de la Independencia', 'Monumento a la Revolución'], 'MXN')
japan=City('Tokyo','Japan','Japanese',37036200,['Tokyo Tower', 'Shibuya Crossing', 'Meiji Shrine'], 'JPY')
usa=City('New York','USA','English',7936530,['Empire States', 'Statue of liberty', 'Central Park'], 'USD')

print(vars(mexico))
print(vars(japan))
print(vars(usa))
```

### 💻 Example Output
```
{'name': 'Mexico City', 'country': 'Mexico', 'language': 'Spanish', 'population': 22752400, 'landmarks': ['Diana', 'Angel de la Independencia', 'Monumento a la Revolución'], 'currency': 'MXN'}
{'name': 'Tokyo', 'country': 'Japan', 'language': 'Japanese', 'population': 37036200, 'landmarks': ['Tokyo Tower', 'Shibuya Crossing', 'Meiji Shrine'], 'currency': 'JPY'}
{'name': 'New York', 'country': 'USA', 'language': 'English', 'population': 7936530, 'landmarks': ['Empire States', 'Statue of liberty', 'Central Park'], 'currency': 'USD'}
```

✅ `__init__()` makes creating rich, detailed objects fast and clean!
![CODEDEX](https://github.com/user-attachments/assets/90809564-b3ea-4fb7-beb7-f36a80aca5a5)
