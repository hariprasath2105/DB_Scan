import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import pickle

# Load dataset
df = pd.read_csv("banking_transactions.csv")

# Features
X = df[['TransactionAmount', 'TransactionTime']]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train DBSCAN
dbscan = DBSCAN(eps=0.8, min_samples=2)
dbscan.fit(X_scaled)

# Save model and scaler
with open("model.pkl", "wb") as f:
    pickle.dump((dbscan, scaler), f)
