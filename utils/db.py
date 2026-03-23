import duckdb

def get_connection():
    return duckdb.connect("sales.db")