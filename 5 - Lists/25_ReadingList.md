# 📚 Reading List and List Methods

## 🛠️ Python List Methods
In addition to built-in functions, Python has several useful list methods:

- `.append(item)` → Adds item to the end of the list
- `.insert(index, item)` → Inserts item at a specific index
- `.remove(item)` → Removes item by value
- `.pop(index)` → Removes item at the specified index

### Example:
```python
dna = ['AUG', 'AUC', 'UCG']

dna.append('UAA')     # ['AUG', 'AUC', 'UCG', 'UAA']
dna.insert(2, 'GAU')  # ['AUG', 'AUC', 'GAU', 'UCG', 'UAA']
dna.remove('AUC')     # ['AUG', 'GAU', 'UCG', 'UAA']
dna.pop(0)            # ['GAU', 'UCG', 'UAA']
```

📌 Methods use dot notation (e.g., `list.append()`), and they only work with lists.

---

## 📋 Common List Methods to Know
| Method       | Description                                      |
|--------------|--------------------------------------------------|
| `.append()`  | Add an item to the end of the list               |
| `.clear()`   | Remove all items from the list                   |
| `.copy()`    | Return a shallow copy of the list                |
| `.count()`   | Count how many times a value appears             |
| `.extend()`  | Append all items from another list               |
| `.index()`   | Return the index of the first matching value     |
| `.insert()`  | Insert an item at a specified position           |
| `.pop()`     | Remove and return item at a specified index      |
| `.remove()`  | Remove the first matching item by value          |
| `.reverse()` | Reverse the list in place                        |
| `.sort()`    | Sort the list in place                           |

---

## 🛒 Reading List Program (`reading_list.py`)
Create a Python program with a book list:

```python
reading_list=['Harry Potter','1984','The Fault in Our Stars','The Mom Test','Life in Code']
print(reading_list)

reading_list.append('Pachinko')
print(reading_list)

reading_list.remove('1984')
print(reading_list)

reading_list.pop(2)
print(reading_list)
```

### 💻 Example Output
```
['Harry Potter', '1984', 'The Fault in Our Stars', 'The Mom Test', 'Life in Code']
['Harry Potter', '1984', 'The Fault in Our Stars', 'The Mom Test', 'Life in Code', 'Pachinko']
['Harry Potter', 'The Fault in Our Stars', 'The Mom Test', 'Life in Code', 'Pachinko']
['Harry Potter', 'The Fault in Our Stars', 'Life in Code', 'Pachinko']

![CODEDEX (3)](https://github.com/user-attachments/assets/c0a63c73-a492-4d73-b951-ca3012b699fb)
