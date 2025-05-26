# 🎒 Pokédex and Class Recap

## ✅ What We Learned
In this chapter, we learned how to:

- Create a class and initialize attributes with `__init__()`
- Create multiple objects using the same class
- Add instance methods to use or modify the data

### Example Structure:
```python
class Student:
    def __init__(self, name, year, enrolled, gpa):
        self.name = name
        self.year = year
        self.enrolled = enrolled
        self.gpa = gpa

    def display_info(self):
        print("The student " + self.name + "'s GPA is " + str(self.gpa) + "!")

    def graduation(self):
        if self.enrolled and self.gpa > 2.5 and self.year == 12:
            print(self.name + " will be able to graduate this year!")
```

---

## 🛒 Pokédex Program (`pokedex.py`)
Create a class to represent a Pokémon entry:

### Define `Pokemon` Class:
```python
# Write code below 💖

class Pokemon:
  def __init__(self, entry, name, types, level, region, height, weight, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.level = level
    self.region = region
    self.height = height
    self.weight = weight
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(self.name + "! " + self.name + "!")

  def display_details(self):
    print("Entry number: ",self.entry)
    print("Name: ", self.name)
    print("Type: " , self.types)
    print("Level: ", self.level)
    print("Region: " +self.region)
    print("Height: ",self.height, "cm")
    print("Weight: ",self.weight, "kg")
    print("Description: " +self.description)
    if self.is_caught==True:
      print(self.name + " has already been caught!")
    else:
      print(self.name + " is missing. Catch it!")

```

### Create Pokémon Objects:
```python
poke1=Pokemon(61, "Poliwhirl", ["Water"], 25, "Kanto", 100, 20.0, "Its two legs are well developed. Even though it can live on the ground, it prefers living in water.", True)
poke2=Pokemon(25, "Pikachu", ["Electric"], 0, "Kanto", 40, 6.0, "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs", True)
poke3=Pokemon(54, "Psyduck", ["Water"], 33, "Kanto", 80, 19.6, "It is constantly wracked by a headache. When the headache turns intense, it begins using mysterious powers.", False)

poke1.speak()
poke1.display_details()

poke3.display_details()
```
### 💻 Example Output
```
Poliwhirl! Poliwhirl!
Entry number:  61
Name:  Poliwhirl
Type:  ['Water']
Level:  25
Region: Kanto
Height:  100 cm
Weight:  20.0 kg
Description: Its two legs are well developed. Even though it can live on the ground, it prefers living in water.
Poliwhirl has already been caught!
Entry number:  54
Name:  Psyduck
Type:  ['Water']
Level:  33
Region: Kanto
Height:  80 cm
Weight:  19.6 kg
Description: It is constantly wracked by a headache. When the headache turns intense, it begins using mysterious powers.
Psyduck is missing. Catch it!
```

![CODEDEX (2)](https://github.com/user-attachments/assets/4d89e105-60a8-4427-a501-2ce5d1cbefce)
