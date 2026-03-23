import pandas as pd
from utils.db import get_connection

def detect_anomalies():
    conn = get_connection()

    df = conn.execute("SELECT * FROM sales").fetchdf()

    mean = df["sales_amount"].mean()
    std = df["sales_amount"].std()

    if std == 0:
        return pd.DataFrame()

    df["z_score"] = (df["sales_amount"] - mean) / std

    anomalies = df[abs(df["z_score"]) > 1.5]

    print("Anomalies:\n", anomalies)

    return anomalies