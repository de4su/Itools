import scapy.all as scapy

class BruteForceAnalyzer:
    def __init__(self):
        self.ssh_failed_connections = []
        self.rdp_failed_connections = []

    def analyze_ssh_traffic(self, pcap_file):
        packets = scapy.rdpcap(pcap_file)
        for packet in packets:
            if packet.haslayer(scapy.TCP) and packet.dport == 22:
                if packet.flags == "R":  # TCP RST flag
                    self.ssh_failed_connections.append(packet)

    def analyze_rdp_traffic(self, pcap_file):
        packets = scapy.rdpcap(pcap_file)
        for packet in packets:
            if packet.haslayer(scapy.TCP) and packet.dport == 3389:
                if packet.flags == "R":  # TCP RST flag
                    self.rdp_failed_connections.append(packet)

    def detect_attacks(self):
        """
        Analyze patterns and detect brute force attacks
        Clustering failed attempts within a time window
        """
        ssh_threshold = 10  # More than 10 failed attempts = suspicious
        rdp_threshold = 10
        
        results = {
            'ssh_attack_detected': len(self.ssh_failed_connections) > ssh_threshold,
            'rdp_attack_detected': len(self.rdp_failed_connections) > rdp_threshold,
            'ssh_failed_count': len(self.ssh_failed_connections),
            'rdp_failed_count': len(self.rdp_failed_connections)
        }
        
        if results['ssh_attack_detected']:
            print(f"[!] SSH Brute-Force Attack Detected: {results['ssh_failed_count']} failed attempts")
        
        if results['rdp_attack_detected']:
            print(f"[!] RDP Brute-Force Attack Detected: {results['rdp_failed_count']} failed attempts")
        
        return results

    def generate_wireshark_filter(self):
        return "tcp.dstport==22 || tcp.dstport==3389"

    def tshark_integration(self, pcap_file):
        filter_command = self.generate_wireshark_filter()
        command = f'tshark -r {pcap_file} -Y "{filter_command}"'
        return command

    def generate_report(self):
        report = f"SSH Failed Connections: {len(self.ssh_failed_connections)}\nRDP Failed Connections: {len(self.rdp_failed_connections)}\n"
        return report

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python pcap_analyzer.py <pcap_file>")
        sys.exit(1)
    
    pcap_file = sys.argv[1]
    analyzer = BruteForceAnalyzer()
    
    print(f"[*] Analyzing PCAP file: {pcap_file}")
    analyzer.analyze_ssh_traffic(pcap_file)
    analyzer.analyze_rdp_traffic(pcap_file)
    
    print("\n" + "="*50)
    print("BRUTE-FORCE ATTACK ANALYSIS REPORT")
    print("="*50 + "\n")
    
    analyzer.detect_attacks()
    print(f"\n{analyzer.generate_report()}")
    print(f"\nWireshark Filter: {analyzer.generate_wireshark_filter()}")
    print(f"tshark Command: {analyzer.tshark_integration(pcap_file)}")