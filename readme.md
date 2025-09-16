# 🩺 Skin Cancer Classification App

A web application that allows users to upload skin images and predicts whether the skin lesion is benign or malignant using a deep learning model. Built with **TensorFlow/Keras** and **Streamlit**.

---

## Features

* Upload images of any size (JPG, JPEG, PNG).
* Automatic image preprocessing (resizing, RGB conversion, normalization).
* Predicts the class of the skin lesion.
* User-friendly and professional interface suitable for medical projects.

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/skin-cancer-classifier.git
cd skin-cancer-classifier
```

2. **Create a virtual environment** (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

> `requirements.txt` should include:
>
> ```
> ```

tensorflow
streamlit
pillow
numpy

````

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
````

1. Open the link provided by Streamlit (usually `http://localhost:8501/`).
2. Upload a skin image.
3. View the prediction results.

---

## Model

* The app uses a pre-trained Keras model saved as `myModel.keras`.
* The model expects images of shape `(224, 224, 3)`, but the app automatically resizes images to fit.

---

## File Structure

```
skin-cancer-classifier/
│
├── app.py               # Streamlit app
├── myModel.keras        # Pre-trained Keras model
├── .gitignore           # Git ignore file
├── requirements.txt     # Python dependencies
└── README.md            # Project description
```

---

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests.

---

## License

This project is licensed under the MIT License.

---

## Screenshots

<img width="623" height="907" alt="image" src="https://github.com/user-attachments/assets/2399aa87-4840-416c-9547-2c47168e3bac" />


