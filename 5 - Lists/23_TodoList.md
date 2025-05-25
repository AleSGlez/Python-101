## Index
- Each item in a list has a position called an index.
- Python lists start at 0 (zero-indexed).

```python
vowels = ['a', 'e', 'i', 'o', 'u']
print(vowels[0])  # 'a'
```

## Negative Index
- Use negative numbers to count from the end.
- `-1` is the last item.

```python
print(vowels[-1])  # 'u'
```

## Slicing
- Get a range of items with `list[start:end]`.
- Includes `start`, excludes `end`.

```python
print(vowels[1:3])  # ['e', 'i']
```

## IndexError
- Occurs when using an index that doesn't exist.

```python
print(vowels[5])  # IndexError
```

---

## Exercise: `todo.py`
Create a todo.py program that will define a todo list that contains the following items:

- '🏦 Get quarters.'
- '🧺 Do laundry.'
- '🌳 Take a walk.'
- 💈 Get a haircut.'
- '🍵 Make some tea.'
- '💻 Complete Lists chapter.'
- '💖 Call mom.'
- '📺 Watch My Hero Academia.'

1) Print the first item and the second item. What did you get?
2) Next, use slicing to print the third, fourth, and fifth items.
3) Try printing out the item at index 9 to see the IndexError before moving on.

```
todo=['🏦 Get quarters.', '🧺 Do laundry.', '🌳 Take a walk.', '💈 Get a haircut.', '🍵 Make some tea.', '💻 Complete Lists chapter.', '💖 Call mom.', '📺 Watch My Hero Academia.']

print(todo[0]) #Print the first item
print(todo[1]) #Print the the second item

print(todo[2:5]) #Use slicing to print the third, fourth, and fifth items

print(todo[9]) #Try printing out the item at index 9 to see the IndexError
```

## 💻 Example Output

```
🏦 Get quarters.
🧺 Do laundry.
['🌳 Take a walk.', '💈 Get a haircut.', '🍵 Make some tea.']
Traceback (most recent call last):
  File "/home/main.py", line 10, in <module>
    print(todo[9])
IndexError: list index out of range
```

![CODEDEX (1)](https://github.com/user-attachments/assets/7daa14ab-6e96-40b3-b318-acdcb1c692d9)
