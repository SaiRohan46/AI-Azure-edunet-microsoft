# 🤖 AI Virtual Mouse – Edunet AI Azure Internship Project

## 📚 Internship Overview: AI Azure by Edunet Foundation

This project was developed as part of the **AI Azure Internship** offered by **Edunet Foundation** in collaboration with **Microsoft** and **AICTE**.

### 🎯 Internship Highlights:

* Delivered over **4 weeks** covering the following:

  * Week 1: AI, ML, DL basics + Microsoft Learn LMS setup
  * Week 2: Supervised & Unsupervised Learning (Regression & Classification)
  * Week 3: Generative AI, Azure Custom Vision hands-on
  * Week 4: Neural Networks, Deep Learning, and Final Project
* Mentorship-driven sessions
* Project-based learning with real-world applications

---

## 🖱️ Project Title: AI Virtual Mouse

### 💡 Objective:

To build an **AI-powered virtual mouse** that enables users to control the system cursor using **hand gestures** tracked by a webcam.

---

## ⚙️ Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* Win32 API (for window control)
* NumPy

---

## 🧠 Features

| Feature                       | Description                                                             |
| ----------------------------- | ----------------------------------------------------------------------- |
| 🖐 Hand Tracking              | Uses MediaPipe to detect and track hand landmarks in real-time          |
| 🖱️ Cursor Movement           | Index finger controls mouse movement via screen-mapped hand coordinates |
| 👆 Click Gesture              | Clicking by bringing index and middle fingers close                     |
| 🖱️ Scroll Control            | Two-finger scroll gesture (up/down)                                     |
| ✊ Drag and Drop               | Thumb + index finger pinch-and-hold for drag actions                    |
| 🪟 Maximize/Minimize Window   | Gesture-based window maximize/minimize using pinch gap detection        |
| 🎚️ Volume Mute + Edge Launch | Special gesture triggers volume mute and opens Microsoft Edge browser   |

---

## 📁 File Structure

```
├── main.py               # Main script to run the AI Virtual Mouse
├── HandTrackingModule.py # Custom hand tracking module using MediaPipe
├── README.md             # Project documentation
```

---

## 🚀 How It Works

1. Open a webcam stream using OpenCV.
2. Use MediaPipe to detect hand landmarks.
3. Map fingertip coordinates to screen resolution.
4. Perform real-time actions:

   * Move cursor with index finger
   * Left click by pinching index & middle fingers
   * Scroll by moving hand with two fingers up
   * Drag using thumb + index
   * Maximize/Minimize windows by adjusting pinch gap
   * Trigger volume mute + Edge browser with 3-finger gesture

---

## 🧪 How to Run

1. Ensure required libraries are installed:

   ```bash
   pip install opencv-python mediapipe pyautogui pywin32 numpy
   ```
2. Run the project:

   ```bash
   python main.py
   ```

---
[Watch the Demo video](demo.mp4)
## 🎓 Developed As Part Of

**AI Azure Internship – May 2025**
**Edunet Foundation** | Microsoft | AICTE
Intern: *Sampathirao Sai Rohan*
Institution: *JNTUK University College of Engineering, Vizianagaram*
Student ID: `STU680bcbf1e6a941745603569`
Internship ID: `INTERNSHIP_174365314467ee0918e7994`

---

## 🔗 Useful Links

* [Edunet Foundation](http://www.edunetfoundation.org/)
* [Microsoft Learn](https://learn.microsoft.com/)
* [MediaPipe Documentation](https://developers.google.com/mediapipe)
* [PyAutoGUI Docs](https://pyautogui.readthedocs.io/)

---

> 🎉 Proud to be a part of this exciting journey in AI Azure
