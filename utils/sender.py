import requests

def send_payloads(url, payloads, param='q'):
    print(f"[+] Sending payloads to {url}")
    for p in payloads:
        try:
            response = requests.get(url, params={param: p}, timeout=5)
            status = response.status_code
            print(f"[{status}] Sent: {p[:60]}{'...' if len(p) > 60 else ''}")
        except Exception as e:
            print(f"[!] Error sending payload: {p[:60]} - {e}")
