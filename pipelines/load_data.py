import pandas as pd
from utils.db import get_connection

def load_data():
    df = pd.read_csv("data/sales_data.csv")

    conn = get_connection()

    conn.execute("DROP TABLE IF EXISTS sales")
    conn.execute("CREATE TABLE sales AS SELECT * FROM df")

    print("Data loaded successfully")