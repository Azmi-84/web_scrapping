from stem import Signal
from stem.control import Controller
import requests

# Function to switch TOR identity
def switch_tor_identity(password="shadow-sprinter", port=9051):
    try:
        with Controller.from_port(port=port) as controller:
            controller.authenticate(password=password)
            controller.signal(Signal.NEWNYM)
            print("[INFO] Switched TOR identity successfully")
    except Exception as e:
        print(f"[ERROR] Failed to switch TOR identity: {e}")
        raise

# Function to fetch the current IP address using the TOR proxy
def fetch_ip_using_proxy():
    proxies = {
        "http": "socks5://127.0.0.1:9050",
        "https": "socks5://127.0.0.1:9050"
    }
    try:
        response = requests.get("http://icanhazip.com", proxies=proxies, timeout=10)
        response.raise_for_status()
        ip = response.text.strip()
        print(f"[INFO] Current IP Address: {ip}")
        return ip
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch IP address: {e}")
        raise

# Function to fetch content from a URL using the TOR proxy
def fetch_using_proxy(url):
    proxies = {
        "http": "socks5://127.0.0.1:9050",
        "https": "socks5://127.0.0.1:9050"
    }
    try:
        # Fetch and print the current IP address
        fetch_ip_using_proxy()

        # Fetch the target content
        response = requests.get(url, proxies=proxies, timeout=10)
        response.raise_for_status()
        print(f"[INFO] HTTP {response.status_code}: Content fetched successfully.")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch URL: {e}")
        raise
