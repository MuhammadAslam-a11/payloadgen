PayloadGen

Custom Payload Generator for Web Exploitation

PayloadGen is a modular Python-based tool designed to automate the generation of evasion-ready payloads for XSS, SQL Injection, and Command Injection attacks. 

It supports advanced encoding, obfuscation, and simulated WAF testing, making it ideal for penetration testers and security researchers.
________________________________________
✨ Features

🔧 Core Payload Modules

•	XSS Payloads

o	Reflected, Stored, and DOM-Based XSS.

o	Bypass techniques: <svg>, srcdoc, null bytes, malformed tags.

•	SQL Injection Payloads

o	Error-based, Union-based, and Blind SQLi.

o	WAF evasion: inline comments, case mixing, encoded characters.

•	Command Injection

o	Linux: ; ls, && whoami, | uname.

o	Windows: | net user, && dir, PowerShell-based payloads.

🌐 Encoding & Obfuscation

•	Supports Base64, URL, Hex, and Unicode encoding.

•	Advanced obfuscation via random comments, spacing tricks, and case variation.
⚙️ Output Options

•	Print to CLI (--output=cli).

•	Export to JSON (--output=json).

•	Copy to clipboard (--output=clipboard).

📊 Bonus Features

•	GUI Mode: Built with Tkinter for visual payload generation.

•	Burp-Style Repeater: Send payloads directly to a target URL with custom query parameters.

•	WAF Simulation: Test payloads against common WAF patterns.
________________________________________
💡 Installation
1.	Clone the repository:

git clone https://github.com/MuhammadAslam-a11/payloadgen.git
cd payloadgen

2.	Install dependencies:

pip install -r requirements.txt

Requirements:

•	Python 3.6+

•	Libraries: pyperclip, requests
________________________________________
🔧 Usage

Command-Line Examples

Generate URL-encoded XSS payloads	

python3 payloadgen.py --xss --encode=url

Obfuscate SQLi and export to JSON	

python3 payloadgen.py --sqli --obfuscate --output=json

Copy CMD Injection payloads to clipboard	

python3 payloadgen.py --cmd --output=clipboard

Simulate WAF blocking	

python3 payloadgen.py --xss --waf-test

Send payloads to a target URL (Burp-style)	

python3 payloadgen.py --sqli --send http://target.com/test --param input

🖼️ GUI Mode

Launch the interactive GUI:

python3 gui.py


Features:

•	Dropdown menus for payload type (XSS/SQLi/CMD).

•	Encoding options (Base64/URL/Hex/Unicode).

•	One-click copy to clipboard.
________________________________________
📂 Project Structure

plaintext


payloadgen/  

├── payloadgen.py    # Main CLI tool  

├── gui.py           # Tkinter GUI  

├── wordlists/       # Custom payload dictionaries  

├── requirements.txt # Dependencies  

└── README.md  
________________________________________
🤝 Contributing

Pull requests and bug reports are welcome! For major changes, open an issue first.
________________________________________
📜 License

This project is licensed under MIT.
________________________________________
📌 Resources

•	Documentation: GitHub Wiki

•	Report Issues: GitHub Issues
________________________________________
🚀 About

Developed by Muhammad Aslam as part of offensive security research.
