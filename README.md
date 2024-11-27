# ARPocalypse

## ARP Spoofing Attack

This project demonstrates a basic ARP (Address Resolution Protocol) spoofing attack using Python and the `scapy` library. ARP spoofing is an attack in which a malicious actor sends fake ARP messages to associate their MAC address with the IP address of a legitimate device, allowing them to intercept or modify network traffic.

### Requirements

Before running the script, you need to install the following dependencies:

- `scapy`

Install it using `pip`:

```bash
pip install scapy
```

## Usage

To run the ARP spoofing attack, execute the following command:

python arp_spoof.py <Target IP> <Gateway IP>

    <Target IP>: The IP address of the target device.
    <Gateway IP>: The IP address of the gateway (usually the router).

Example

python arp_spoof.py 192.168.1.5 192.168.1.1

This will spoof the ARP tables of the target device (192.168.1.5) and the gateway (192.168.1.1).
---
## Restoring the Network

When you stop the script, it will attempt to restore the original ARP entries and return the network to normal.
