import nmap
import socket
import threading

class PortScanner:
    def __init__(self, target):
        self.target = target
        self.nm = nmap.PortScanner()
        self.open_ports = []

    def scan_port(self, port):
        try:
            # Attempt to connect to the port
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((self.target, port))
                if result == 0:
                    print(f"Port {port} is open")
                    self.open_ports.append(port)
                    self.grab_banner(port)
                else:
                    print(f"Port {port} is closed")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    def grab_banner(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.target, port))
                s.settimeout(1)
                banner = s.recv(1024).decode().strip()
                print(f"Banner from port {port}: {banner}")
        except Exception as e:
            print(f"Could not grab banner from port {port}: {e}")

    def scan(self, ports):
        threads = []
        for port in ports:
            thread = threading.Thread(target=self.scan_port, args=(port,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def service_detection(self):
        for port in self.open_ports:
            self.nm.scan(self.target, str(port))
            service = self.nm[self.target]['tcp'][port]['name']
            version = self.nm[self.target]['tcp'][port]['version']
            print(f"Service on port {port}: {service} (Version: {version})")

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    ports_to_scan = range(1, 1025)  # Scanning first 1024 ports
    scanner = PortScanner(target)
    scanner.scan(ports_to_scan)
    scanner.service_detection()