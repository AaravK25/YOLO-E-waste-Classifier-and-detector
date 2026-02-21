# ♻️ E-Waste Component Detection using YOLOv26n

This repository documents my learning journey in **Computer Vision** and **YOLO-based object detection**.

The project focuses on detecting and classifying laptop/PC components into:

* ♻️ Recyclable
* 🔧 Repairable
* 🔁 Reusable

using **YOLOv26n (Ultralytics)**.

---

## 📌 Project Overview

* Model: **YOLOv26n**
* Framework: **Ultralytics 8.4.14**
* Purpose: Multi-class object detection for categorized e-waste components
* GPU: NVIDIA RTX 3050 Laptop GPU (4GB VRAM)

---

## 📊 Dataset Details

### Dataset Split

| Set   | Percentage | Images |
| ----- | ---------- | ------ |
| Train | 88%        | 7644   |
| Valid | 8%         | 728    |
| Test  | 4%         | 364    |

---

## 🖼️ Preprocessing & Augmentations

### Preprocessing

* ✅ Auto-Orient applied
* ✅ Resize: `512x512`
* ✅ Fill with center crop

### Augmentations (3 outputs per training image)

* 🔄 Horizontal Flip
* 🔄 Vertical Flip
* 🎨 Saturation: -25% to +25%
* 💡 Brightness: -23% to +23%
* 🔹 Noise: Up to 0.1% of pixels

---

## 🧠 Model Summary

```
YOLOv26n (fused)
Layers: 122  
Parameters: 2,389,850  
GFLOPs: 5.3  
```

**Environment:**

* Python 3.10.19
* torch 2.11.0.dev20260209+cu128
* CUDA 12.8
* GPU: RTX 3050 Laptop GPU (4096 MiB)

---

## 📈 Overall Validation Performance

| Metric    | Value     |
| --------- | --------- |
| Precision | 0.681     |
| Recall    | 0.763     |
| mAP@50    | 0.752     |
| mAP@50-95 | **0.641** |

Inference Speed:

* ⚡ 0.3ms preprocess
* ⚡ 2.3ms inference
* ⚡ 0.2ms postprocess

---

## 📉 Training Curves

<img src="images/training_metrics.png" width="100%">

*(Losses decreasing steadily and mAP stabilizing around 0.64 mAP50-95)*

---

## 📊 Confusion Matrix

<img src="images/confusion_matrix.png" width="100%">

*Strong diagonal dominance indicating good per-class separation.*

---

## 🏆 Strong Performing Classes (mAP50-95 ≥ 0.85)

* HardDiskDrive_Repairable (0.908)
* LCDScreen_Repairable (0.945)
* LVDSCable_Repairable (0.854)
* Processor_Repairable (0.854)
* RAMCover_Repairable (0.862)
* RAM_Reusable (0.878)
* SSD_Recyclable (0.894)
* SSD_Reusable (0.872)
* TouchPad_Recyclable (0.837)
* HeatSink_Recyclable (0.87)

---

## ⚠️ Low Performing Classes (Data Scarcity Issue)

Some classes have very low image counts (1–3 images), which caused instability:

* Keyboard_Recyclable
* WebCam_Recyclable
* CPUFan_Reusable
* Motherboard_Repairable
* SSD_Repairable

These require more data for reliable learning.

---

## 🚀 Key Observations

* Model converges cleanly without instability.
* Precision and Recall are well balanced.
* Strong performance considering:

  * 4GB VRAM constraint
  * 50+ fine-grained classes
* Small class imbalance affects minority categories.

---

## 🔮 Future Improvements

* Add more samples for low-frequency classes.
* Try larger models (YOLOv26s / YOLOv26m).
* Apply class-balanced sampling.
* Experiment with longer training.
* Tune augmentation intensity.

---

## 🛠️ How to Run For Inference

```bash
pip install ultralytics
```

```python
from ultralytics import YOLO

model = YOLO("Best.pt")

model.train(
    data="data.yaml",
    imgsz=512,
    epochs=100,
    batch=16
)
```

---

## 🎯 Goal of This Repository

This project is part of my deep dive into:

* Computer Vision
* Object Detection
* Model Evaluation
* Dataset Engineering
* Real-world deployment constraints (low VRAM training)

---

If you're reading this — feedback is welcome.
This is a continuous learning project.

---


Tell me what level you want — clean, advanced, or elite.
