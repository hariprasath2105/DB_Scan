# DBSCAN-Based Anomaly Detection in Banking

This project implements a simple **Anomaly Detection system** for banking transactions using **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** algorithm. The system is deployed using **Flask** with a visually enhanced HTML/CSS frontend.

---

## Objective

Detect unusual transactions (possible fraud) based on:
- **Transaction Amount**
- **Transaction Time**

---
## Tech Stack

- Python
- Flask
- HTML, CSS
- Scikit-learn
- Pandas
- Numpy
- Matplotlib

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-003366?style=for-the-badge&logo=matplotlib&logoColor=white)

---
## Project Structure

```
DBSCAN_AnomalyDetection/
│
├── model.py          
├── app.py             
├── model.pkl          
├── templates/
│   ├── index.html       
│   └── result.html     
├── static/
│   └── style.css         
├── dataset.csv         
└── README.md            
```

---

## Model Details

- **Algorithm**: DBSCAN (unsupervised)
- **Features used**: Transaction Amount, Transaction Time
- **Output**: `Normal Transaction ✅` or `Anomaly Detected ❌`

---

## How It Works

1. Input is scaled using `StandardScaler`
2. The trained DBSCAN model checks if input fits into any known dense cluster
3. If not part of any cluster → flagged as **anomaly (`-1`)**

---

## Sample Normal Inputs

| Amount | Time |
|--------|------|
| 105    | 11.5 |
| 110    | 12   |
| 100    | 10   |

These inputs are within the dense cluster area.

---

## Sample Anomaly Inputs

| Amount | Time |
|--------|------|
| 500    | 5    |
| 1000   | 1    |
| 1200   | 2    |

These are far from any known dense cluster in training data.

---

## Run the App

```bash
# Step 1: Train the model
python model.py

# Step 2: Run the Flask app
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

## Input

<img width="517" height="431" alt="image" src="https://github.com/user-attachments/assets/48ac410f-7caf-4086-8374-33e709784d91" />

---
## Output 

<img width="517" height="431" alt="image" src="https://github.com/user-attachments/assets/791031e1-0f89-446c-b4f0-72d7215ec93f" />

---
