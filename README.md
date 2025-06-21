PayloadGen: Custom Payload Generator for Web Exploitation

PayloadGen is a modular Python-based tool that automates the generation of web exploitation payloads for:

XSS (Reflected, Stored, DOM-Based)
SQL Injection (Error-Based, Union-Based, Blind)
Command Injection (Linux & Windows)

The tool provides evasion-ready output, supports encoding, obfuscation, simulated WAF testing, and even includes a GUI interface and Burp-style HTTP payload testing.

✨ Features

🔧 Core Modules

XSS Payloads:
Reflected, Stored, and DOM-Based

Bypass techniques using <svg>, srcdoc, malformed tags, null bytes

SQLi Payloads:
Error-based, Union-based, Blind SQLi

WAF evasion: comments, case tricks, encoded characters

Command Injection:
Linux: ; ls, && whoami, | uname
Windows: | net user, && dir, PowerShell-based injections

🌐 Encoding & Obfuscation

Supports Base64, URL, Hex, and Unicode encodings
Obfuscation via inline comments, spacing tricks, casing

⚙️ Output Options

Print to CLI
Export to JSON
Copy to clipboard

📊 Bonus Features

✅ GUI using Tkinter (select module, encoding, generate payloads visually)
✅ Burp-style Repeater: Send payloads directly to a live URL with custom query param
✅ Simulated WAF Testing: Test which payloads are blocked by common WAF patterns

💡 Installation

git clone https://github.com/engalisaleh95/payloadgen.git
cd payloadgen
pip install -r requirements.txt

requirements.txt:
pyperclip
requests


🔧 How to Use

Generate Encoded XSS Payloads
python3 payloadgen.py --xss --encode=url

Obfuscate SQLi and Export to JSON
python3 payloadgen.py --sqli --obfuscate --output=json

Copy CMD Injection Payloads to Clipboard
python3 payloadgen.py --cmd --output=clipboard

Combine All
python3 payloadgen.py --xss --sqli --cmd --encode=base64 --output=cli

Simulate WAF Blocking
python3 payloadgen.py --xss --waf-test

Send Payloads to Target URL (Simulates Burp Repeater)

python3 payloadgen.py --sqli --send http://target.com/test --param input

🖼️ GUI Mode (Tkinter)

Launch the GUI:

python3 gui.py

Features:

Select payload type: XSS, SQLi, CMD

Choose encoding: None, Base64, URL, Hex, Unicode

Enable obfuscation

Copy to clipboard

Simulated WAF test built-in