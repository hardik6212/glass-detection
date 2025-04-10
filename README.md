
```markdown
# 🔍 GlassNoGlass YOLOv8 Detector with Streamlit

An interactive web app built using **Streamlit** and **YOLOv8** (Ultralytics) for detecting the presence or absence of glass in images. Upload an image, optionally convert it to greyscale, run inference, view results, and download the annotated output.

---

## 🚀 Features

- ✅ Upload image (JPG, JPEG, PNG)
- ✅ Optional greyscale conversion
- ✅ YOLOv8 model inference
- ✅ Annotated image preview
- ✅ Download annotated result

---

## 🗂️ Project Structure

```
GlassNoGlassApp/
│
├── app.py                 # Streamlit application
├── requirements.txt       # Project dependencies
└── model/
    └── best.pt            # Trained YOLOv8 model
```

---

## 📦 Requirements

- Python 3.8 or higher
- [Streamlit](https://streamlit.io)
- [OpenCV](https://opencv.org)
- [Ultralytics YOLOv8](https://docs.ultralytics.com)

### 🔧 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Run the App

```bash
streamlit run app.py
```

Then, open the URL shown in your terminal (usually http://localhost:8501) to access the app in your browser.

---

## 🧠 Model Setup

Place your YOLOv8 trained model file in the `model/` directory.

```bash
GlassNoGlassApp/
└── model/
    └── best.pt
```

> You can train your model using:
```bash
yolo task=detect mode=train model=yolov8n.pt data=your_data.yaml epochs=50 imgsz=640
```

---

## 🖼️ How It Works

1. Upload an image
2. Toggle greyscale conversion (optional)
3. The app runs the YOLO model and shows the detection
4. Download the annotated result

---
<!-- 
## 🧾 Example

| Input | Output |
|-------|--------|
| Upload: ![](https://via.placeholder.com/100x100?text=Input) | Annotated: ![](https://via.placeholder.com/100x100?text=Detected) | -->

---

## 📃 License

This project is licensed under the MIT License.

---

## 🙌 Credits

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [Streamlit](https://streamlit.io)

---

## 👨‍💻 Author

Created by Ashutosh, Hardik, Shiva, Hem and Zaigham - feel free to reach out for improvements or collaborations!
```

Let me know if you want to include deployment instructions (like on Streamlit Cloud or Docker) or auto-demo screenshots.
