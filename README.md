# PacketSniffer

**PacketSniffer** is a simple network analysis tool designed to capture and inspect network packets in real-time. It provides insight into raw network traffic and demonstrates how packets can be captured and logged directly from a network interface.

---

## 🚨 Disclaimer
This tool is for **educational purposes only**. Unauthorized use to monitor or intercept private communications without explicit permission is illegal and unethical. Use responsibly and in compliance with all applicable laws.

---

## 📝 Features
- **Real-Time Packet Capture**: Collect network packets as they traverse your network interface.
- **Minimal Configuration**: No complex options or filters—ready to use out of the box.
- **Cross-Platform Support**: Works on Linux, macOS, and Windows with administrative privileges.
- **Lightweight**: Simple Python script with minimal dependencies.

---

## 🖥️ Requirements
- Python 3.x or later
- Required libraries:
  - `scapy` (for packet sniffing and manipulation)

Install the required library using:
```bash
pip install scapy
```

---

## 🔧 Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/atphosphate/PacketSniffer.git
   cd PacketSniffer
   ```

2. Run the script with administrative privileges:
   ```bash
   sudo python packetsniffer.py -i <interface>
   ```

---

## 📂 File Structure
- **`packetsniffer.py`**: Main script for capturing and logging packets.
- **`README.md`**: Documentation for the tool.

---

## 📖 Usage
To capture packets, simply execute the script with administrative privileges:
```bash
sudo python packetsniffer.py
```

The script will start sniffing packets and display relevant information about each captured packet in real-time.

---

## 🔍 Example Output
```bash
[*] Captured Packet: Source: 192.168.1.1 -> Destination: 192.168.1.100
[*] Packet Details: Protocol: TCP, Port: 443
[*] Captured Packet: Source: 192.168.1.100 -> Destination: 192.168.1.1
[*] Packet Details: Protocol: UDP, Port: 53
...
```

Captured packets will display source and destination IPs, protocol details, and other basic information depending on how your script parses packet data.

---

## 🚀 Future Enhancements
- Add support for packet filtering (e.g., by protocol, port, or IP).
- Include a feature to save packets to a file for later analysis.
- Enhance packet parsing for detailed header and payload analysis.
- Integrate with Wireshark-compatible `.pcap` files.

---

## 🛡️ Legal and Ethical Usage
This tool should only be used in authorized testing environments or with the network owner's permission. Misuse for unauthorized packet capture can lead to legal repercussions.

---

## 🧑‍💻 Contribution
Contributions are welcome! To improve or extend this project:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request for review.
