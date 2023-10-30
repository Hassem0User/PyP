from scapy.all import ARP, Ether, srp

def scan_local_network(ip_range):
    # Create an ARP request packet to discover local devices
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast Ethernet frame

    packet = ether / arp

    # Send the packet and capture responses
    result = srp(packet, timeout=3, verbose=0)[0]

    # Extract the IP and MAC addresses of the responding devices
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

ip_range = "192.168.1.0/24"  # Define subnet interface

active_devices = scan_local_network(ip_range)

for device in active_devices:
    print(f"IP Address: {device['ip']}, MAC Address: {device['mac']}")
