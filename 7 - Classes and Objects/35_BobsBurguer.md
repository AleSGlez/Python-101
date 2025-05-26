# 🍔 Bob's Burgers and Creating Objects

## 🧱 What is an Object?
An **object** is an instance of a class. Once you've defined a class, you can create multiple objects from it, each with its own values.

### Example:
```python
class Student:
    student_id = 0
    name = ''
    year = 0
    gpa = 0.0
    enrolled = False

ferris = Student()
ferris.name = 'Ferris Bueller'
```
Each object can have unique data but share the same structure defined by the class.

To inspect an object’s attributes, use:
```python
print(vars(ferris))
```

---

## 🛒 Bob's Burgers Program (`bobs_burgers.py`)
Create and customize restaurant objects based on the `Restaurant` class you created earlier:

```python
# Write code below 💖
class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = False
  
bobs_burgers= Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

WanWanSakaba= Restaurant()
WanWanSakaba.name = 'WanWan Sakaba'
WanWanSakaba.category = 'Japanese Style Restaurant'
WanWanSakaba.rating = 4.8
WanWanSakaba.delivery = True

CasaTono= Restaurant()
CasaTono.name = 'La Casa de Toño'
CasaTono.category = 'Mexican Restaurant'
CasaTono.rating = 4.7
CasaTono.delivery = True

print(vars(bobs_burgers))
print(vars(WanWanSakaba))
print(vars(CasaTono))
```

### 💻 Example Output
```
{'name': "Bob's Burgers", 'category': 'American Diner', 'rating': 4.7, 'delivery': False}
{'name': 'WanWan Sakaba', 'category': 'Japanese Style Restaurant', 'rating': 4.8, 'delivery': True}
{'name': 'La Casa de Toño', 'category': 'Mexican Restaurant', 'rating': 4.7, 'delivery': True}
```

![CODEDEX](https://github.com/user-attachments/assets/0be74546-a7d9-41c8-9d13-a6ee7ece7a9e)
