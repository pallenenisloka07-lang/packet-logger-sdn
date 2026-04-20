# Packet Logger using SDN Controller (POX)

## Overview
This project implements a packet logger using the POX SDN controller. It captures packets from the network, extracts header information, identifies protocols, and logs them in real time.

## Features
- Captures PacketIn events from switches
- Extracts MAC addresses
- Identifies protocols (ARP, IPv4, TCP, UDP, ICMP)
- Logs packet details
- Forwards packets using OFPP_FLOOD

## Tools Used
- Python
- POX SDN Controller
- Mininet

## How to Run

1. Start POX Controller
cd ~/pox
./pox.py misc.packet_logger

2. Start Mininet
sudo mn --topo single,3 --controller remote

3. Test Connectivity
pingall

## Expected Output
- Packet logs displayed in POX terminal
- 0 percent packet loss in Mininet

## Screenshots

### POX Output
![POX Output](screenshots/pox_output.png)

### Mininet Output
![Mininet Output](screenshots/mininet_output.png)

