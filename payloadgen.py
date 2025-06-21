# payloadgen.py

import argparse
from modules import xss_generator, sqli_generator, cmd_generator, encoder
from utils import helpers
from utils import sender
from utils import waf_filter



def main():
    parser = argparse.ArgumentParser(
        description="Custom Payload Generator for Web Exploitation"
    )

    # Payload type flags
    parser.add_argument('--xss', action='store_true', help='Generate XSS payloads')
    parser.add_argument('--sqli', action='store_true', help='Generate SQLi payloads')
    parser.add_argument('--cmd', action='store_true', help='Generate Command Injection payloads')

    # Encoding & obfuscation
    parser.add_argument('--encode', choices=['base64', 'url', 'hex', 'unicode'],
                        help='Apply encoding to payloads')
    parser.add_argument('--obfuscate', action='store_true',
                        help='Apply obfuscation to payloads')

    # Output formats
    parser.add_argument('--output', choices=['cli', 'json', 'clipboard'],
                        default='cli', help='Choose output method')
    
    parser.add_argument('--send', metavar='URL', help='Send payloads to a given URL (simulates Burp Repeater)')
    parser.add_argument('--param', metavar='PARAM', default='q', help='Query parameter name to inject payloads')

    parser.add_argument('--waf-test', action='store_true',
                        help='Run simulated WAF test against generated payloads')

    args = parser.parse_args()

    payloads = []

    if args.xss:
        payloads.extend(xss_generator.generate_payloads())
    if args.sqli:
        payloads.extend(sqli_generator.generate_payloads())
    if args.cmd:
        payloads.extend(cmd_generator.generate_payloads())

    # Apply encoder/obfuscator
    if args.encode:
        payloads = [encoder.apply_encoding(p, args.encode) for p in payloads]
    if args.obfuscate:
        payloads = [encoder.apply_obfuscation(p) for p in payloads]

    # Output
    if args.output == 'cli':
        for p in payloads:
            print(p)
    elif args.output == 'json':
        helpers.export_to_json(payloads)
    elif args.output == 'clipboard':
        helpers.copy_to_clipboard(payloads)

    if args.send:
        sender.send_payloads(args.send, payloads, param=args.param)

    if args.waf_test:
        print("\n[+] Running simulated WAF test...")
        results = waf_filter.test_payloads_against_waf(payloads)

        print(f"\n🚫 Blocked by WAF: {len(results['blocked'])}")
        for b in results["blocked"]:
            print(f"  [BLOCKED] {b}")

        print(f"\n✅ Passed WAF: {len(results['passed'])}")
        for p in results["passed"]:
            print(f"  [PASSED] {p}")






if __name__ == "__main__":
    main()
