# Detection Evasion Techniques (Educational)

## Network-Level Evasion

### 1. Non-Standard Ports
- Use ports like 443 (HTTPS) or 53 (DNS) instead of 4444
- Blends with normal traffic

### 2. Traffic Obfuscation
- Base64 encode commands
- Encrypt C2 communication with XOR or AES
- Use HTTP/HTTPS tunneling

### 3. Timing Jitter
- Add random delays between communications
- Avoids pattern-based detection

## Host-Level Evasion

### 1. Process Hiding
- Rename process to look legitimate
- Run as background service

### 2. String Obfuscation
- Avoid obvious strings like "C2", "backdoor"
- Use encoded or encrypted strings

### 3. Anti-Analysis
- Detect virtual machines
- Detect debuggers

## Example: Basic XOR Encoding

```python
def xor_encrypt(data, key=0x42):
    return bytes([b ^ key for b in data])

# Usage
command = "whoami"
encrypted = xor_encrypt(command.encode())
# Decrypt on client side
decrypted = xor_encrypt(encrypted)
```

## Detection Methods (Defensive Perspective)

1. Network monitoring for unusual outbound connections
2. Endpoint detection and response (EDR)
3. Behavioral analysis
4. Command-line auditing
5. Network traffic baselining

## Legal and Ethical Notice

These techniques are for **educational purposes only** to understand attacker methodology and improve defensive security posture.

**Unauthorized use is illegal and unethical.**
