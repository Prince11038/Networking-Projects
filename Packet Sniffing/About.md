# Network Packet Sniffer and Analyzer

## Overview

This Python script captures and analyzes network packets on a specified interface. It supports filtering by protocol (`TCP`, `UDP`, or `ICMP`) and provides detailed insights into the packet's source, destination, protocol, ports, and payload data. The tool is interactive and designed for network monitoring, debugging, and educational purposes.

---

## Features

- **Protocol Filtering:** Filter packets by `TCP`, `UDP`, or `ICMP` for focused analysis.
- **Detailed Analysis:** Displays source and destination IPs, ports, protocol type, and packet payload in both hexadecimal and decoded formats.
- **Interactive Interface Selection:** Lists all available network interfaces for the user to choose from.
- **Packet Capture Limit:** Allows capturing a specific number of packets or continuous capture until stopped.

---

## Prerequisites

### Requirements

1. **Python 3.7 or above**
2. Required Python libraries:
   - `scapy`

### Installing Scapy
To install Scapy, run:
```bash
pip install scapy
```

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/network-packet-sniffer.git
   cd network-packet-sniffer
   ```

2. Run the script:
   ```bash
   python packet_sniffer.py
   ```

3. Follow the prompts:
   - Choose a network interface for sniffing.
   - Specify the protocol (`TCP`, `UDP`, or `ICMP`).
   - Define the number of packets to capture (`0` for continuous capture).

4. Stop continuous capture with `Ctrl+C`.

---

## Output

### Example Output

**Interface Selection:**
   ```text
   Available Interfaces:
1. \Device\NPF_{5445E37F-7B46-48D7-8631-252D12047964}
2. \Device\NPF_{C7876ED4-E1B3-4E00-B75E-DE6093B5444B}
3. \Device\NPF_{9549EB2A-1F59-42EB-94C0-4B1918F3B3D1}
4. \Device\NPF_{7FEDAAD1-D633-4B6B-89AE-20A541968C9B}
5. \Device\NPF_{74D0484C-5B5C-46EC-963E-ED500E5B217C}
6. \Device\NPF_{676BEF76-9F1B-4630-890D-F53DB8262522}
7. \Device\NPF_Loopback
Enter the interface index for sniffing: 4
   ```

2. **Protocol Filtering:**
   ```text
   Enter the service protocol to filter (TCP/UDP/ICMP): tcp
   ```

3. **Packet Analysis:**
   ```text
   Source IP:      192.168.1.2      >>> Destination IP: 192.168.1.1     
   Protocol:       TCP             
   Source Port:    12345            >>> Destination Port: 80             
   Payload Hex Data:
   48 65 6c 6c 6f 20 57 6f 72 6c 64
   Decoded Payload Data:
   Hello World
   ```

---

## How It Works

1. **Interface Selection:**  
   The script lists all available network interfaces and allows the user to select one for packet sniffing.

2. **Protocol Filtering:**  
   Filters packets by the specified protocol (`TCP`, `UDP`, or `ICMP`) using Scapy's `filter` parameter.

3. **Packet Analysis:**  
   For each captured packet:
   - Displays source and destination IP addresses.
   - Extracts and prints the protocol, source and destination ports (if applicable), and payload.
   - Formats payload data in both hexadecimal and decoded (if possible) formats.

4. **Continuous or Limited Capture:**  
   The user can define the number of packets to capture or run the sniffer indefinitely.

---

## Known Limitations

- Decoded payload may not always be human-readable due to binary or encrypted data.
- Requires root or administrative privileges to sniff network traffic on some systems.
- May not capture packets if there is no network traffic on the selected interface or protocol.

---

## Contributing

Contributions are welcome! If you'd like to enhance this project:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---


## Author
Prince Kumar Singh 
Feel free to reach out for questions, feedback, or suggestions!
