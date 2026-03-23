from utils.db import get_connection

def run_checks():
    conn = get_connection()

    results = {}

    results["row_count"] = conn.execute(
        "SELECT COUNT(*) FROM sales"
    ).fetchone()[0]

    results["null_sales"] = conn.execute(
        "SELECT COUNT(*) FROM sales WHERE sales_amount IS NULL"
    ).fetchone()[0]

    results["zero_sales"] = conn.execute(
        "SELECT COUNT(*) FROM sales WHERE sales_amount = 0"
    ).fetchone()[0]

    print("DQ Results:", results)

    return results