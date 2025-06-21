import urllib.parse
import base64

def apply_encoding(payload, method):
    if method == 'base64':
        return base64.b64encode(payload.encode()).decode()
    elif method == 'url':
        return urllib.parse.quote(payload)
    elif method == 'hex':
        return ''.join(['\\x'+format(ord(c), 'x') for c in payload])
    elif method == 'unicode':
        return ''.join(['\\u'+format(ord(c), '04x') for c in payload])
    return payload

def apply_obfuscation(payload):
    # Simple obfuscation by inserting spaces or comments (basic example)
    return payload.replace(" ", "/**/")
