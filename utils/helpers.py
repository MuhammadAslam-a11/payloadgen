import json
import pyperclip

def export_to_json(payloads, filename='payloads/sample_payloads.json'):
    with open(filename, 'w') as f:
        json.dump(payloads, f, indent=2)
    print(f"Payloads exported to {filename}")

def copy_to_clipboard(payloads):
    combined = '\n'.join(payloads)
    pyperclip.copy(combined)
    print("Payloads copied to clipboard.")
