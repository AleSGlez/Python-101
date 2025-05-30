# 📦 Python Packages - Python Course Notes

## 🧩 What Are Packages?
- **Modules** = `.py` files with functions, classes, variables.
- **Packages** = folders containing multiple modules with a similar purpose.

> A package is recognized by Python if it includes an `__init__.py` file.

### 📚 Examples of Popular Packages:
- **Data Analysis**: NumPy, Pandas, SciPy
- **Data Visualization**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: Scikit-learn, TensorFlow
- **Web Scraping**: Beautiful Soup
- **Game Dev**: Pygame
- **Chatbots/NLP**: NLTK, OpenAI
- **Automation**: OS, Requests

These tools make Python incredibly versatile!

---

## 📥 Installing Packages with `pip3`
`pip3` is the recommended package installer for Python 3.

### Install a package:
```bash
pip3 install matplotlib
```
If that doesn’t work, try:
```bash
pip install matplotlib
```

Then you can import the package in your Python code:
```python
import matplotlib
import matplotlib.pyplot
```
Use **dot notation** to access modules and functions inside packages.

> 📝 Note: Online editors may not support pip. Use VS Code or a terminal to follow along.

---

## 🧪 Practice Activity: `wiki.py`

### Steps:
1. Open a code editor like **VS Code**.
2. Check if `pip3` is installed:
```bash
pip3 --version
```
3. Install the `wikipedia` package:
```bash
pip3 install wikipedia
```

4. Create a file called `wiki.py` and write:
```python
import wikipedia

result = wikipedia.summary("Python (programming language)", sentences=2)
print(result)
```

5. Run the file:
```bash
python3 wiki.py
```

### 🔍 Other Search Ideas:
- "Philosophy of life"
- "Galaxy"
- "Artificial Intelligence"

---

```Python
import wikipedia

print (wikipedia.summary("Galaxy"))
```
###Preview of the output on the terminal
![image](https://github.com/user-attachments/assets/16d27871-0ee4-4f5e-8c97-9a0a75fdba90)
