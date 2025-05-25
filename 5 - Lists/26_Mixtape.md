# 🔁 Iterating Over a List
You can iterate through a list in multiple ways. Here are the two most common:

### 1. `for-in` Loop
Loop directly through the items:
```python
snowfall = [0.3, 0.0, 0.0, 1.2, 3.9, 2.2, 0.8]

for i in snowfall:
    print(i)
```
Each `i` represents an item in the list. Output:
```
0.3
0.0
0.0
1.2
3.9
2.2
0.8
```

### 2. `for-in` with `range()` and `len()`
Loop through indices:
```python
for i in range(len(snowfall)):
    print(snowfall[i])
```
Here, `i` is the index, and `snowfall[i]` accesses the item at that position.

---

## 🛒 Mixtape Program (`mixtape.py`)
Create a Python program with a playlist of songs using a theme:

```python
# 💿 Theme: Indie Travel Songs
playlist = [
  'Porches - rangerover',
  'Mount Eerie - You Swan, Go On',
  'Carolyn Polachek - Look at Me Now',
  'Pinegrove - Darkness',
  'LVL UP - Spirit Was',
  'Mitski - First Love / Late Spring'
]

for song in playlist:
    print(song)
```

### 💻 Example Output
```
Imagination - Foster The People
Drink Up - Train
Formidable - Twenty one Pilots
Can You Feel The Love Tonight - Simple Plan
```
![CODEDEX (4)](https://github.com/user-attachments/assets/89f36487-64d9-449a-9bfc-1d498e59466c)
