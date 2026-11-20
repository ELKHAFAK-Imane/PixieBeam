<p align="center">
  <img src="Capture.PNG" alt="PixieBeam Logo" width="130"/>
</p>

# ✨ PixieBeam — Intelligent Medical Contouring & Segmentation

> *"Where clinical precision meets a touch of magic."*

**PixieBeam** is a standalone Python desktop application designed for rapid, high-precision CT DICOM medical image contouring and anatomical segmentation across **16 calibrated Hounsfield Unit (HU)** tissue classes.

### 🪄 The Inspiration Behind PixieBeam
Inspired by **Tinker Bell’s spark, speed, and keen intelligence**, PixieBeam transforms tedious manual radiology contouring into an effortless, accurate workflow. Just like a precise beam of light isolating the finest details, the tool rapidly delineates targeted anatomical structures—from delicate soft tissues and vasculature to dense cortical bone—bringing speed, clarity, and a touch of magic to medical imaging analysis.

### 🎯 Core Capabilities
* **Rapid & Detailed Segmentation:** Instant thresholding across 16 clinical tissue, fluid, and bone classes (`-1000 HU` Air to `+3000+ HU` Tooth Enamel).
* **CT DICOM Integration:** Seamless `.dcm` slice loading with an interactive, ergonomic GUI.
* **Custom Golden Theme:** Clean, distraction-free interface supporting Light, Dark, and System modes.
* **Clinical Reference & Documentation:** Built-in Hounsfield Unit scale guide and full architectural specifications in [`PixieBeam Technical Presentation & Documentation.pdf`](PixieBeam%20Technical%20Presentation%20%26%20Documentation.pdf).

### 🛠️ Tech Stack
* **Language:** Python 3
* **GUI Framework:** CustomTkinter, Tkinter
* **Medical & Image Processing:** `pydicom`, `NumPy`, `Pillow (PIL)`
