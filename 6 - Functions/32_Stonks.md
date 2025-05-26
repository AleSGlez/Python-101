# 📈 Stonks and Variable Scope in Python

## 🎯 What is Scope?
Scope defines **where a variable can be used** in your program.

### Two Main Types of Scope:
- **Local Scope** – A variable defined inside a function (can only be used inside that function)
- **Global Scope** – A variable defined outside any function (can be accessed throughout the program)

### Example:
```python
def add(x, y):
    answer = x + y
    return answer

print(answer)  # ❌ NameError: 'answer' is not defined
```
`answer` is a **local variable**, so it cannot be accessed outside the function.

### Global Variable Example:
```python
answer = 0

def add(x, y):
    answer = x + y
    return answer

add(3, 4)
print(answer)  # ✅ Prints 0 (global variable is unaffected)
```
Even though both variables are named `answer`, the one inside the function is separate from the global one.

---

## 🛒 Stock Analysis Program (`stock_analysis.py`)
Perform a simplified time series analysis on AMC stock data for January 2023:

```python
#Stocks prices (in dollars) for each of these weekdays (1 to 20)
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

#Functions
def price_at(x):
  price=stock_prices[x-1]
  return price

def max_price(a,b):
  return max(stock_prices[a-1:b])

def min_price(a, b):
  return min(stock_prices[a - 1 : b])

#Tests
print(price_at(5))
print(max_price(1,5))
print(min_price(18,20))
```

### 💻 Example Output
```
34.68
36.09
44.21
```

✅ These functions help analyze the stock data over a specific range of days, showing how scope keeps each function's variables separate unless explicitly returned.

![CODEDEX (10)](https://github.com/user-attachments/assets/4eb61c63-88c3-4f17-94cf-08265287605b)
