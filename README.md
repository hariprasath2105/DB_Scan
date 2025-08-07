# 🏦 DBSCAN-Based Anomaly Detection in Banking

This project implements a simple **Anomaly Detection system** for banking transactions using **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** algorithm. The system is deployed using **Flask** with a visually enhanced HTML/CSS frontend.

---

## 📌 Objective

Detect unusual transactions (possible fraud) based on:
- **Transaction Amount**
- **Transaction Time**

---

## 📂 Project Structure

```
DBSCAN_AnomalyDetection/
│
├── model.py              # Trains DBSCAN model and saves using pickle
├── app.py                # Flask application logic
├── model.pkl             # Saved model and scaler (Pickle format)
├── templates/
│   ├── index.html        # Input form page with gradient styling
│   └── result.html       # Result display page
├── static/
│   └── style.css         # Custom CSS styles
├── dataset.csv           # (Optional) Sample transaction data used
└── README.md             # This file
```

---

## 📊 Model Details

- **Algorithm**: DBSCAN (unsupervised)
- **Features used**: Transaction Amount, Transaction Time
- **Output**: `Normal Transaction ✅` or `Anomaly Detected ❌`

---

## 💡 How It Works

1. Input is scaled using `StandardScaler`
2. The trained DBSCAN model checks if input fits into any known dense cluster
3. If not part of any cluster → flagged as **anomaly (`-1`)**

---

## ✅ Sample Normal Inputs

| Amount | Time |
|--------|------|
| 105    | 11.5 |
| 110    | 12   |
| 100    | 10   |

These inputs are within the dense cluster area.

---

## ❌ Sample Anomaly Inputs

| Amount | Time |
|--------|------|
| 500    | 5    |
| 1000   | 1    |
| 1200   | 2    |

These are far from any known dense cluster in training data.

---

## 🚀 Run the App

```bash
# Step 1: Train the model
python model.py

# Step 2: Run the Flask app
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

## 🌐 Tech Stack

- Python, Flask
- Scikit-learn
- HTML5, CSS3 (with gradient UI)
- Pickle (for model saving)

---

## 🧠 Future Improvements

- Add real-time anomaly visualization
- Integrate database for transaction logging
- Use advanced anomaly detection methods (e.g., Isolation Forest, Autoencoders)