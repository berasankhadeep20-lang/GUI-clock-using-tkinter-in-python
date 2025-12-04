<div align="center">

# 🕰️ Python GUI Clocks Collection

### A dual showcase of Digital and Analog timekeeping using Python & Tkinter.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![Math](https://img.shields.io/badge/Module-Math-orange?style=for-the-badge)
![Time](https://img.shields.io/badge/Module-Time-yellow?style=for-the-badge)

[View Projects](#-project-catalog) • [How to Run](#-how-to-run) • [Code Insights](#-code-insights)

</div>

---

## 📖 About The Project

This repository demonstrates two different approaches to building GUI applications in Python using **Tkinter**. It serves as a perfect example of how to handle **Main Loops**, **Canvas Drawing**, and **Time Manipulation**.

1.  **Analog Clock:** Uses trigonometry (`sin`, `cos`) to calculate and draw moving hands on a canvas in real-time.
2.  **Digital Clock:** Uses string formatting to update a label widget every second.

---

## 📸 Screenshots

| **Analog Clock** | **Digital Clock** |
|:---:|:---:|
|  | 

[Image of digital clock LED display]
 |
| *(Replace this text with your screenshot)* | *(Replace this text with your screenshot)* |

---

## 📂 Project Catalog

| File Name | Type | Description |
| :--- | :--- | :--- |
| **`#gui clock(analog)tkinter in python.py`** | 🎨 Canvas | Draws a dynamic clock face. Uses `math` to calculate hand angles based on current time. |
| **`gui clock(digital)tkinter in python.py`** | 🔢 Widget | A minimal digital display using the `time.strftime` method for accurate formatting. |

---

## 🚀 How to Run

**⚠️ Important Note on Filenames:**
Because the filenames contain spaces and special characters (like `#` and `()`), you must enclose the filenames in **quotes** when running them in your terminal.

1.  **Clone the repository**
    ```sh
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Run the Analog Clock**
    ```sh
    python "#gui clock(analog)tkinter in python.py"
    ```

3.  **Run the Digital Clock**
    ```sh
    python "gui clock(digital)tkinter in python.py"
    ```

---

## 🧠 Code Insights

### The Math Behind the Analog Clock
To make the hands move correctly, we convert time into angles (radians):
* **Hours:** `(hours + minutes/60) * 30` degrees.
* **Minutes:** `(minutes + seconds/60) * 6` degrees.
* **Seconds:** `seconds * 6` degrees.

We then use **Sine** and **Cosine** functions to determine the (x, y) coordinates for the end of each clock hand on the canvas.

### The Logic Behind the Digital Clock
The digital clock uses a simple recursive function:
```python
def clock():
    # Get current time
    # Update Label text
    label.after(1000, clock) # Recursively call itself after 1000ms (1 second)
