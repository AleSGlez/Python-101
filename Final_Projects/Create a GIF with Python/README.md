# 🖼️ Create a GIF with Python

## 🧠 Prerequisites
- Python fundamentals
- Command line basics
- Python 3.10
- `imageio` version 2.16.2

⏳ Estimated Time: 30 minutes

---

## 🎬 Introduction
GIFs (Graphics Interchange Format) are animated images made by sequencing multiple pictures. They’re great for memes, reactions, or fun visual projects. In this project, you’ll learn how to create your own GIF using just 6 lines of Python code!

We’ll use:
- A **list**
- A **for loop**
- The **imageio** library

---

## 📦 Install the ImageIO Library
Use the terminal or command prompt:
```bash
pip3 install imageio
```

✅ Verify installation:
```python
import imageio
```
No errors? You're good to go!

---

## 📝 Writing the Program
Create a file: `create_gif.py`

### Step-by-step Code:
```python
import imageio.v3 as iio

filenames = ['team-pic1.png', 'team-pic2.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration = 500, loop = 0)
```

### Breakdown:
- `filenames`: list of image filenames
- `images`: stores image data
- `iio.imread()`: reads images from disk
- `iio.imwrite()`: creates the GIF

**Parameters for `imwrite()`:**
- `'team.gif'`: name of output GIF
- `images`: image data list
- `duration=500`: display time per image (ms)
- `loop=0`: loop forever

Make sure image files are in the **same folder** as the script.

---

## ▶️ Running the Program
Navigate to the project folder:
```bash
cd path/to/folder
```
Run the script:
```bash
python3 create_gif.py
```

🎉 `team.gif` will appear in the folder.

---

## 🔧 Make It Your Own
- Try using **your own images**!
- Add more images (3 or more).
- Make sure all images have the **same dimensions**.

### Modify:
```python
filenames = ['img1.png', 'img2.png', 'img3.png']
```

---

## 🎉 Wrapping Up
Congratulations! You created a GIF in Python using:
- A list
- A for loop
- The imageio library

You now have a tool to make custom GIFs without paid apps. Show off your creations and tag `@codedex_io` on Twitter or IG!
