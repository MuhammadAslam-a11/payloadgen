import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import pyperclip
from modules import xss_generator, sqli_generator, cmd_generator, encoder
from utils import waf_filter

def generate_payloads():
    payloads = []

    # Get user selections
    selected_type = attack_type.get()
    selected_encoding = encoding.get()
    apply_obf = obfuscate_var.get()
    run_waf_test = waf_test_var.get()

    # Generate payloads
    if selected_type == "XSS":
        payloads = xss_generator.generate_payloads()
    elif selected_type == "SQLi":
        payloads = sqli_generator.generate_payloads()
    elif selected_type == "CMD":
        payloads = cmd_generator.generate_payloads()

    # Apply encoding
    if selected_encoding != "None":
        payloads = [encoder.apply_encoding(p, selected_encoding.lower()) for p in payloads]

    # Apply obfuscation
    if apply_obf:
        payloads = [encoder.apply_obfuscation(p) for p in payloads]

    # WAF simulation
    waf_result = None
    if run_waf_test:
        waf_result = waf_filter.test_payloads_against_waf(payloads)
        payloads = waf_result["passed"] + waf_result["blocked"]

    # Show results
    output_box.delete(1.0, tk.END)
    for p in payloads:
        output_box.insert(tk.END, p + "\n")

    if run_waf_test:
        output_box.insert(tk.END, "\n---\n[WAF TEST RESULTS]\n")
        output_box.insert(tk.END, f"\n🚫 Blocked by WAF: {len(waf_result['blocked'])}\n")
        for b in waf_result["blocked"]:
            output_box.insert(tk.END, f"  [BLOCKED] {b}\n")
        output_box.insert(tk.END, f"\n✅ Passed WAF: {len(waf_result['passed'])}\n")
        for p in waf_result["passed"]:
            output_box.insert(tk.END, f"  [PASSED] {p}\n")

def copy_to_clipboard():
    content = output_box.get(1.0, tk.END).strip()
    if content:
        pyperclip.copy(content)
        messagebox.showinfo("Copied", "Payloads copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No payloads to copy.")

# GUI Setup
root = tk.Tk()
root.title("PayloadGen GUI")

# Row 0 - Payload Type
tk.Label(root, text="Payload Type:").grid(column=0, row=0, sticky="w", padx=10, pady=5)
attack_type = ttk.Combobox(root, values=["XSS", "SQLi", "CMD"], width=20)
attack_type.set("XSS")
attack_type.grid(column=1, row=0, padx=10, pady=5)

# Row 1 - Encoding Type
tk.Label(root, text="Encoding:").grid(column=0, row=1, sticky="w", padx=10, pady=5)
encoding = ttk.Combobox(root, values=["None", "Base64", "URL", "Hex", "Unicode"], width=20)
encoding.set("None")
encoding.grid(column=1, row=1, padx=10, pady=5)

# Row 2 - Options
obfuscate_var = tk.BooleanVar()
tk.Checkbutton(root, text="Obfuscate Payloads", variable=obfuscate_var).grid(column=0, row=2, sticky="w", padx=10)

waf_test_var = tk.BooleanVar()
tk.Checkbutton(root, text="Simulate WAF Filter", variable=waf_test_var).grid(column=1, row=2, sticky="w", padx=10)

# Row 3 - Buttons
ttk.Button(root, text="Generate Payloads", command=generate_payloads).grid(column=0, row=3, padx=10, pady=10)
ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(column=1, row=3, padx=10, pady=10)

# Row 4 - Output Box
output_box = scrolledtext.ScrolledText(root, width=100, height=25)
output_box.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

root.mainloop()