# 🚀 Mars Orbiter and Function Parameters

## 📥 Parameters and Arguments
Functions become much more powerful when they can take **input values**. This is done using:

- **Parameters** → variables declared in the function definition
- **Arguments** → values passed in when calling the function

### Example Without Parameters:
```python
def happy_birthday():
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday dear friend")
    print("Happy birthday to you")
```
Always prints the same thing.

### Example With Parameters:
```python
def happy_birthday(name):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday dear " + name)
    print("Happy birthday to you")

happy_birthday("Lillian")
```
Now it's personalized! Here, `name` is the **parameter**, and `'Lillian'` is the **argument**.

💡 We've been using arguments already:
```python
print("Yo!")  # 'Yo!' is the argument passed to print()
```

---

## 🛒 Rocket Conversion Program (`rocket.py`)
You're working at NASA. You need to convert kilometers to miles correctly so your orbiter doesn't burn up!

```python
def distance_to_miles(distance):
    miles = distance / 1.609
    print(miles)

distance_to_miles(10000)
```

### 💻 Example Output
```
6215.040397762586
```

✅ This function takes a `distance` (in kilometers) and prints the equivalent in miles using the correct conversion rate.


![CODEDEX (8)](https://github.com/user-attachments/assets/0bf7069f-42e2-46f7-9260-19c7216f33e5)
