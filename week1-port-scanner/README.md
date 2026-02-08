# Week 1: Port Scanner

TCP port scanner with service detection, banner grabbing, and optional nmap integration.

## Features

- Multithreaded port scanning
- Service identification
- Banner grabbing
- Nmap integration for detailed service detection
- JSON report generation
- Configurable timeout and thread count

## Usage

Basic scan:
```bash
python port_scanner.py 127.0.0.1
```

Scan specific port range:
```bash
python port_scanner.py 192.168.1.1 -s 1 -e 1000
```

Use nmap for service detection:
```bash
python port_scanner.py scanme.nmap.org --nmap
```

Save results to file:
```bash
python port_scanner.py 10.0.0.1 -o results.json
```

Adjust performance:
```bash
python port_scanner.py 192.168.1.1 -t 200 --timeout 0.5
```

## Requirements

See requirements.txt

## Legal Notice

Only scan systems you own or have explicit permission to test.