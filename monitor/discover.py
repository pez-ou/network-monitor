# monitor/discover.py

import subprocess
import ipaddress
import time
from pathlib import Path

def is_host_alive(ip):
    try:
        result = subprocess.run(['ping', '-n', '1', '-w', '500', str(ip)],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode == 0
    except Exception:
        return False

def discover_ips(base_cidr="192.168.1.0/24", duration=30):
    network = ipaddress.ip_network(base_cidr, strict=False)
    active_ips = []
    start_time = time.time()

    for ip in network.hosts():
        if time.time() - start_time > duration:
            print("⏱️ Temps écoulé pour la découverte réseau.")
            break
        if is_host_alive(ip):
            print(f"[+] {ip} est actif")
            active_ips.append(str(ip))

    # Écrit dans targets.txt
    target_file = Path(__file__).parent / "targets.txt"
    with open(target_file, "w") as f:
        for ip in active_ips:
            f.write(f"{ip}\n")
    print(f"\n✅ Découverte terminée. {len(active_ips)} IPs actives enregistrées dans targets.txt.")
