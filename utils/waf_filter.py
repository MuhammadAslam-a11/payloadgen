import re

# Simulated WAF Rules (basic pattern matching)
BLOCK_PATTERNS = [
    r"<script.*?>",          # blocks script tags
    r"\bOR\b\s+1=1",         # blocks OR 1=1
    r"(?i)union\s+select",   # blocks UNION SELECT
    r";",                    # blocks semicolon
    r"\|\|?",                # blocks pipe and double pipe
    r"\&\&?",                # blocks ampersand and double ampersand
    r"alert\(",              # blocks alert() as signature
    r"xp_cmdshell",          # blocks dangerous SQL function
    r"base64",               # blocks base64 encoded payloads
]

def test_payloads_against_waf(payloads):
    results = {"blocked": [], "passed": []}

    for payload in payloads:
        blocked = False
        for pattern in BLOCK_PATTERNS:
            if re.search(pattern, payload, re.IGNORECASE):
                blocked = True
                break
        if blocked:
            results["blocked"].append(payload)
        else:
            results["passed"].append(payload)

    return results
