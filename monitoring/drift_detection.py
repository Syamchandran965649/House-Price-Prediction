import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset
from pathlib import Path
import json

# -----------------------------
# Load datasets
# -----------------------------
reference_data = pd.read_csv("data/processed/processed_data.csv")
current_data = pd.read_csv("monitoring/prediction_logs.csv")

# -----------------------------
# Remove columns not required
# -----------------------------
ignore_columns = [
    "Timestamp",
    "property_id",
    "Predicted_Price"
]

reference_data = reference_data.drop(columns=ignore_columns, errors="ignore")
current_data = current_data.drop(columns=ignore_columns, errors="ignore")

# -----------------------------
# Keep common columns
# -----------------------------
common_columns = reference_data.columns.intersection(current_data.columns)

reference_data = reference_data[common_columns]
current_data = current_data[common_columns]

# -----------------------------
# Generate Report
# -----------------------------
report = Report(metrics=[DataDriftPreset()])

my_eval = report.run(
    reference_data=reference_data,
    current_data=current_data
)

Path("monitoring").mkdir(exist_ok=True)

my_eval.save_html("monitoring/drift_report.html")

# -----------------------------
# Extract Results
# -----------------------------
result = my_eval.dict()

# Optional: uncomment to inspect full structure
# print(json.dumps(result, indent=2, default=str))

# First metric is the overall DriftedColumnsCount summary
summary_metric = result["metrics"][0]
number_of_drifted = int(summary_metric["value"]["count"])
drift_share = summary_metric["value"]["share"]
total_columns = len(result["metrics"]) - 1  # exclude the summary entry itself

drift_detected = drift_share >= 0.5  # matches drift_share=0.5 threshold used above

# Per-column drift details
column_drift_details = []
for m in result["metrics"][1:]:
    column_drift_details.append({
        "column": m["config"]["column"],
        "method": m["config"]["method"],
        "score": m["value"]
    })

print("="*60)
print("DRIFT DETECTION REPORT")
print("="*60)

if drift_detected:
    print("Status              : DRIFT DETECTED")
else:
    print("Status              : NO DRIFT")

print(f"Drifted Features    : {number_of_drifted}/{total_columns}")
print(f"Drift Percentage    : {drift_share*100:.2f}%")
print("="*60)
print("Per-column drift scores:")
for c in column_drift_details:
    print(f"  {c['column']:20s} ({c['method']:30s}) : {c['score']:.4f}")
print("="*60)

with open("monitoring/drift_summary.txt", "w") as f:
    f.write("DRIFT DETECTION REPORT\n")
    f.write("="*50 + "\n")
    f.write(f"Status : {'DRIFT DETECTED' if drift_detected else 'NO DRIFT'}\n")
    f.write(f"Drifted Features : {number_of_drifted}/{total_columns}\n")
    f.write(f"Drift Percentage : {drift_share*100:.2f}%\n")
    f.write("\nPer-column drift scores:\n")
    for c in column_drift_details:
        f.write(f"  {c['column']:20s} ({c['method']:30s}) : {c['score']:.4f}\n")

print("HTML Report saved to monitoring/drift_report.html")
print("Summary saved to monitoring/drift_summary.txt")