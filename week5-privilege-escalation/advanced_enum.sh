#!/bin/bash

echo "=================================="
echo "Advanced Privilege Escalation Enumeration"
echo "=================================="
echo ""

echo "[*] System Information"
uname -a
cat /etc/issue

echo ""
echo "[*] Current User & Groups"
id
groups

echo ""
echo "[*] Checking SUID binaries..."
find / -perm -4000 -type f 2>/dev/null

echo ""
echo "[*] Checking SGID binaries..."
find / -perm -2000 -type f 2>/dev/null

echo ""
echo "[*] Checking sudo permissions..."
sudo -l 2>/dev/null

echo ""
echo "[*] Checking writable /etc/passwd..."
test -w /etc/passwd && echo "[!] /etc/passwd is writable!" || echo "[+] /etc/passwd not writable"

echo ""
echo "[*] Checking for capabilities..."
getcap -r / 2>/dev/null

echo ""
echo "[*] Checking writable directories in PATH..."
echo $PATH | tr ':' '\n' | while read dir; do
    if [ -w "$dir" ]; then
        echo "[!] Writable: $dir"
    fi
done

echo ""
echo "[*] Checking for running processes as root..."
ps aux | grep root

echo ""
echo "[*] Checking cron jobs..."
ls -la /etc/cron* 2>/dev/null
cat /etc/crontab 2>/dev/null

echo ""
echo "[*] Done"
