from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained DBSCAN model and scaler
with open("model.pkl", "rb") as f:
    dbscan, scaler = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        amount = float(request.form['amount'])
        time = float(request.form['time'])

        # Preprocess input
        data = np.array([[amount, time]])
        scaled_data = scaler.transform(data)

        # Calculate distance from core samples
        distances = np.linalg.norm(dbscan.components_ - scaled_data, axis=1)
        is_anomaly = all(distances > dbscan.eps)

       
        result = "Anomaly Detected ❌" if is_anomaly else "Normal Transaction ✅"

        return render_template('result.html', result=result, amount=amount, time=time)

    except Exception as e:
        return f"Error processing input. Please enter valid values.<br><br><code>{e}</code>"

if __name__ == '__main__':
    app.run(debug=True)
