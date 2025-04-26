# monitor/checker.py

from ping3 import ping
from pathlib import Path

def check_targets():
    results = []
    targets_path = Path(__file__).parent / "targets.txt"

    if not targets_path.exists():
        print("❌ Le fichier targets.txt est introuvable.")
        return []

    with open(targets_path, "r") as f:
        targets = [line.strip() for line in f if line.strip()]

    for target in targets:
        response = ping(target, timeout=1)
        status = "UP" if response else "DOWN"
        results.append((target, status))

    return results
