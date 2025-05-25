# 🔧 Built-in Functions
Python has useful built-in functions for working with lists:

- `len(list)` → Returns the number of items.
- `max(list)` → Returns the largest item.
- `min(list)` → Returns the smallest item.

### Example:
```python
stock1_prices = [2.52, 2.44, 2.32, 2.41, 2.51, 2.50, 2.44]
stock2_prices = [8.36, 8.31, 8.21, 8.21, 8.25, 8.11, 8.13]

print(len(stock1_prices))  # 7
print(max(stock1_prices))  # 2.52
print(min(stock2_prices))  # 8.11
```
These functions are fast and work well even with large lists.

💡 Not all built-in functions work with lists, but `len()`, `min()`, and `max()` are especially useful.

---

## 🛒 Inventory Program (`inventory.py`)
Create a Python program that helps the North Pole elves analyze LEGO parts before the holidays:

```python
lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]

#Which LEGO part are the elves running low on? Use min() to find out.
print(min(lego_parts))

#Is there a LEGO part that the elves are overstocking? Use max() to find out.
print(max(lego_parts))
```
Each number represents the quantity of a different colored LEGO part.

### 💻 Example Output
```
589
92232
```

![CODEDEX (2)](https://github.com/user-attachments/assets/bce3321a-ec5a-4a40-9ac4-265926e1fbbf)
