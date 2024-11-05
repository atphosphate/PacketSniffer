import scapy.all as scapy
from scapy.layers import http
from scapy.all import Raw

def listen_packets(iface):
    scapy.sniff(iface=iface, store=False, prn=analyze_packets)
    #prn = callback function

def analyze_packets(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(Raw):
            print(packet[Raw].load)

listen_packets("eth0")