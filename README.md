# 🎯 Confusion Matrix Generator

A **clean, user-friendly, and publication-ready Confusion Matrix Generator** built using **Streamlit**.
This tool allows users to **manually construct confusion matrices with clear row–column mapping** and export them as **high-quality images** suitable for **research papers, reports, and presentations**.

---

## 🚀 Features

* 🔢 Dynamic number of classes (2–20)
* 🧭 **Clear Row–Column Mapping**

  * Rows → Actual classes
  * Columns → Predicted classes
* 🎨 Modern UI with glassmorphism design
* 🖼️ High-quality image export:

  * PNG
  * JPG
  * PDF
* 📐 Publication-ready resolution (300 / 600 DPI)
* ☁️ Fully compatible with **Streamlit Cloud**
* ❌ No OCR, no CSV, no external system dependencies

---

## 🖥️ User Interface Overview

### Step 1: Configure Classes

* Select number of classes
* Enter class names (comma-separated)

### Step 2: Enter Confusion Matrix Values

* Inputs are explicitly labeled:

  * `R1 → C1`, `R1 → C2`, etc.
* No ambiguity about where values go

### Step 3: Export Settings

* Choose image format
* Select DPI
* Download high-quality output

---

## 📸 Screenshots


![Home Screen](https://raw.githubusercontent.com/ak-0283/confusion_matrix_generator/refs/heads/main/screenshot/Screenshot%202025-12-24%20225512.png)

---

![Matrix Input](https://raw.githubusercontent.com/ak-0283/confusion_matrix_generator/refs/heads/main/screenshot/Screenshot%202025-12-24%20225526.png)

---

![](https://raw.githubusercontent.com/ak-0283/confusion_matrix_generator/refs/heads/main/screenshot/Screenshot%202025-12-24%20230334.png)

---

![Export Output](https://raw.githubusercontent.com/ak-0283/confusion_matrix_generator/refs/heads/main/screenshot/Screenshot%202025-12-24%20225542.png)


---

## 🧑‍💻 Tech Stack

* **Python**
* **Streamlit**
* **NumPy**
* **Matplotlib**

---


## 🌐 Live Demo
👉 [Click here](https://confusion-matrix-generator.streamlit.app/)

---

## 📂 Project Structure

```
confusion-matrix-generator/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/   (optional)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/confusion-matrix-generator.git
cd confusion-matrix-generator
```

---

### 2️⃣ Install Dependencies

> Only **one command required**.

```bash
pip install -r requirements.txt
```

**`requirements.txt`**

```
streamlit
numpy
matplotlib
```

---

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser.

---

## ☁️ Deployment (Streamlit Cloud)

1. Push this repository to GitHub
2. Go to **Streamlit Cloud**
3. Select the repository
4. Choose `app.py`
5. Click **Deploy**

✔ No additional configuration required
✔ Lightweight & fast deployment

---

## 🧠 How It Works (Conceptual)

* Users manually enter confusion matrix values to avoid OCR errors
* Explicit row–column labeling ensures correctness
* Matplotlib renders a clean confusion matrix
* Images are exported using in-memory buffers to preserve quality

---

## 🧪 Use Cases

* Machine Learning evaluation
* Emotion detection projects
* Medical image classification (brain tumor, cancer, etc.)
* Academic research papers
* College major / minor projects
* Reports & presentations

---

## 🤝 Contribution Guidelines

Contributions are welcome and easy!

### How to Contribute

1. Fork the repository
2. Clone your fork
3. Install dependencies using `requirements.txt`
4. Make your changes
5. Submit a pull request

### Suggested Enhancements

* Percentage-normalized confusion matrix
* Auto-fill diagonal values
* Light/Dark mode toggle
* Watermark / branding
* Side-by-side comparison of models

---

## 📌 Notes

* This project intentionally avoids OCR to ensure:

  * Deployment stability
  * Data correctness
  * Low user frustration
* Designed with **clarity, accuracy, and usability** as top priorities

---

## 📜 License

This project is open-source and free to use for **educational and research purposes**.

---

## 🙌 Acknowledgement

Built with ❤️ using **Streamlit** for a clean and interactive user experience.

---
