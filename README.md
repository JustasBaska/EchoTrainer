# 🎯 EchoTrainer

**EchoTrainer** is an interactive memory training app that challenges users to **reproduce visual shapes from memory**. Built with Streamlit, it blends cognitive science with playful interactivity to sharpen your visual recall and drawing accuracy.

---

## 🧠 Concept

- You are shown a shape for a few seconds.
- The shape disappears, and you must **redraw it from memory**.
- After submission, EchoTrainer:
  - Compares your drawing to the original
  - Calculates a **similarity score** (using SSIM)
  - Displays **side-by-side visual feedback**
  - Lets you **play again** at the same difficulty level

Difficulty levels vary both **shape complexity** and **memorization time**.

---

## 🚀 Features

- 🖼️ Random shape preview based on difficulty
- ⏱️ Timed memory phase
- ✏️ Interactive canvas for drawing input
- ⚖️ Image similarity scoring with SSIM
- 📊 Score feedback + visual comparison
- 🔁 "Play Again" reset and replay loop
- 📁 Organized for easy expansion (scoring, gamification, etc.)

---

## 🛠️ Tech Stack

| Tool/Library            | Purpose                                |
|-------------------------|----------------------------------------|
| Streamlit               | UI and app structure                   |
| streamlit-drawable-canvas | Interactive drawing canvas             |
| NumPy, Pillow (PIL)     | Image processing                       |
| OpenCV                  | Optional preprocessing (future use)   |
| scikit-image            | SSIM-based image similarity scoring   |
| Python 3.11             | Core programming language              |

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/EchoTrainer.git
cd EchoTrainer
