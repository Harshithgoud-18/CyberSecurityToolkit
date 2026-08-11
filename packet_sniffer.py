"""
Packet Sniffer Module

This module captures network packets using Scapy
and displays the source IP, destination IP,
and protocol.
"""

#Third-Party Libraries
from scapy.all import sniff
from scapy.layers.inet import IP


def get_protocol(proto):
    """
    Convert protocol number to protocol name.

    Args:
        proto (int): IP protocol number.

    Returns:
        str: Protocol name.
    """
    if proto == 1:
        return "ICMP"
    elif proto == 6:
        return "TCP"
    elif proto == 17:
        return "UDP"
    else:
        return str(proto)


def packet_callback(packet):
    """
    Process each captured packet.

    Args:
        packet: Captured network packet.
    """
    
     # Check whether packet contains an IP layer
    if packet.haslayer(IP):

        print("=" * 40)
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)
        print("Protocol       :", get_protocol(packet[IP].proto))
        print("=" * 40)


def start_sniffer():
    """
    Capture and display five network packets.
    """


    print("Capturing 5 packets...\n")

    sniff(
        prn=packet_callback,
        count=5,
        store=False
    )