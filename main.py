from pipelines.load_data import load_data
from data_quality.checks import run_checks
from anomaly_detection.detect import detect_anomalies
from ai_explanation.explain import explain
from alerts.alert import send_alert

def run_pipeline():
    print("Starting pipeline...\n")

    load_data()

    run_checks()

    anomalies = detect_anomalies()

    if not anomalies.empty:
        for _, row in anomalies.iterrows():
            explanation = explain(row)
            send_alert(explanation)
    else:
        print("No anomalies found")

if __name__ == "__main__":
    run_pipeline()