# **Packet Sniffer with Protocol Analysis**

This Python script is a **packet sniffer** that captures network packets and analyzes them based on their protocol type (TCP, UDP, ICMP, ARP, DNS, or others). It logs details such as source and destination IPs, ports, protocol-specific information, and payload data into a log file.

---

## **Features**
1. **Protocol-Specific Analysis**:
   - Identifies and tracks packets for protocols like TCP, UDP, ICMP, ARP, and DNS.
   - Logs source and destination IPs, ports, MAC addresses, and DNS queries.

2. **Payload Handling**:
   - Logs payloads in both hexadecimal and decoded formats (UTF-8 or Latin-1 if decodable).

3. **Custom Filters**:
   - Supports user-defined protocol filters (e.g., TCP, UDP, ICMP) to capture specific traffic types.

4. **Interactive Interface Selection**:
   - Lists available network interfaces for the user to select from.

5. **Logging**:
   - Saves packet details to a timestamped log file for later analysis.

6. **Capture Options**:
   - Supports continuous capture or a user-defined number of packets.

7. **Packet Capture Summary**:
   - Displays the count of packets captured per protocol at the end of the session.

---

## **Setup and Requirements**

### **Dependencies**
- Python 3.x
- Scapy library

Install the required library using:
```bash
pip install scapy
```

### **Run the Script**
1. Clone or download the script file.
2. Execute the script:
   ```bash
   python packet_sniffer.py
   ```

---

## **How to Use**

1. **Interface Selection**:
   - The script lists all available network interfaces on your machine.
   - Enter the index of the desired interface for sniffing traffic.

2. **Set Protocol Filter**:
   - You can specify a filter for protocols (e.g., `TCP,UDP,ICMP`).
   - Leave it blank to capture all traffic.

3. **Packet Capture Limit**:
   - Specify the number of packets to capture.
   - Enter `0` for continuous capture (use `Ctrl+C` to stop).

4. **View Captured Details**:
   - The script logs and displays captured packet details, including:
     - Source and destination IPs.
     - Ports, MAC addresses, and DNS queries.
     - Payload data in both hex and decoded text formats.

5. **Stop Capture**:
   - Use `Ctrl+C` to stop the capture at any time.

6. **Check Log File**:
   - The details are saved to a log file named `packet_log_<timestamp>.txt`.

---

## **Log File Structure**

The log file contains details of each packet captured. Below is an example structure:

```
Source IP:       192.168.1.1       >>> Destination IP:   192.168.1.100
Protocol:        TCP
Source Port:     443               >>> Destination Port: 52345
Payload Hex Data:
48 65 6c 6c 6f 20 57 6f 72 6c 64 21
Decoded Payload Data:
Hello World!
--------------------------------------------------
```

---

## **Notes**
- The script relies on **Scapy**, a powerful packet manipulation tool.
- Root or administrative privileges may be required to capture packets on some systems.
- Ensure you comply with local laws and organizational policies when capturing network traffic.

---

## **Improvements**
Future updates could include:
- Multi-threaded packet analysis for higher performance.
- Support for additional protocols.
- Graphical user interface (GUI).

---

## **Disclaimer**
This tool is for educational and authorized use only. Unauthorized packet capturing may violate privacy laws. Use responsibly.
