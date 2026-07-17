import pandas as pd
import subprocess
import os

LOG_FILE = "monitoring/prediction_logs.csv"

def monitor_predictions():

    if not os.path.exists(LOG_FILE):
        return

    df = pd.read_csv(LOG_FILE)

    # Run drift detection every 100 predictions
    if len(df) % 100 == 0:
        print("Running Drift Detection...")
        subprocess.run(
            ["python", "monitoring/drift_detection.py"]
        )