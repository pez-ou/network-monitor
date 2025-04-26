# main.py

from monitor.discover import discover_ips
from monitor.checker import check_targets

def main():
    print("🔍 Étape 1 : Scan du réseau (30 secondes)...")
    discover_ips(base_cidr="192.168.1.0/24", duration=30)

    print("\n📡 Étape 2 : Vérification des hôtes...")
    results = check_targets()

    print("\n📋 Résultats du monitoring :")
    for ip, status in results:
        print(f" - {ip} : {status}")

if __name__ == "__main__":
    main()
