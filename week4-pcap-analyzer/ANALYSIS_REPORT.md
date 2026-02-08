# PCAP Traffic Analysis Report

## Objective
Analyze network traffic to identify brute-force attack patterns

## Tools Used
- Scapy for packet analysis
- Wireshark filters for traffic inspection

## Methodology
1. Extract TCP packets on ports 22 (SSH) and 3389 (RDP)
2. Identify RST flags indicating failed connection attempts
3. Count failed attempts per source IP
4. Flag sources exceeding threshold as suspicious

## Key Indicators
- High volume RST packets to SSH/RDP ports
- Multiple connection attempts from same source IP
- Short time intervals between attempts

## Wireshark Filter
```
tcp.dstport==22 || tcp.dstport==3389
```

## Findings
Use this tool to analyze your own PCAP files and document findings here.
