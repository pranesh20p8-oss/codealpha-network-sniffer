# Basic Network Sniffer

A beginner-friendly network sniffer built with Python and Scapy. It captures network packets on an authorized network interface and displays useful packet information.

## Features

- Captures network packets
- Displays source IP address
- Displays destination IP address
- Identifies TCP, UDP, and ICMP protocols
- Displays source port
- Displays destination port
- Displays payload size

## Technologies Used

- Python
- Scapy
- Npcap

## How It Works

The program uses Scapy to capture packets from the network interface.

For each IP packet, it extracts:

- Source IP
- Destination IP
- Protocol
- Source port
- Destination port
- Payload size

The program captures 10 packets and then stops.

## Installation

Install the required Python package:

```bash
pip install -r requirements.txt