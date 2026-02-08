#!/bin/bash
echo "Linux Privilege Escalation Checker"
echo "==================================="
echo ""
echo "[*] Checking SUID binaries..."
find / -perm -4000 -type f 2>/dev/null
echo ""
echo "[*] Checking sudo permissions..."
sudo -l 2>/dev/null
echo ""
echo "[*] Checking writable /etc/passwd..."
test -w /etc/passwd && echo "[!] /etc/passwd is writable!" || echo "[+] /etc/passwd not writable"
echo ""
echo "[*] Done"