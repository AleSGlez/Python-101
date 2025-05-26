# 🍽️ Restaurants and Introduction to Classes

## 🧱 What is a Class?
A **class** is like a **blueprint** for creating objects with shared structure and behavior.

Use a class when you want to:
- Group data and behavior in one place
- Model real-world objects (students, cars, restaurants)
- Create many instances with the same structure but different data

### Why not use lists?
```python
student_1 = [1001, 'Asiqur', 10, 3.7, True]
```
You can't tell what each value means at a glance.

### With Classes:
```python
class Student:
    name = ''
    year = 0
    gpa = 0.0
    enrolled = False
```
Much clearer! You know what each variable represents.

---

## 🛒 Restaurant Class Program (`restaurants.py`)
Let's build a class to store restaurant data for a food delivery app.

```python
class Restaurant:
    name = ''       # Name of the restaurant (str)
    category = ''   # Type of food (str)
    rating = 0.0    # Customer rating (float)
    delivery = False  # Delivery available? (bool)
```

This defines a template for restaurant data. You’ve just created a **custom data type**! 🧠

✅ This file won’t show any output yet — it only defines the structure. In the next step, you’ll create objects from this class and start working with real data.
