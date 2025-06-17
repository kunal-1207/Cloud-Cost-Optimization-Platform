import os
import json

def export(report):
    os.makedirs("metrics", exist_ok=True)
    with open("metrics/metrics.json", "w") as f:
        json.dump(report, f)
