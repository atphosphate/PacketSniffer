import scapy.all as scapy
from scapy.layers import http
from scapy.all import Raw
import optparse

def get_info():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface", dest="interface", help="interface to change")
    return parse_object.parse_args()


def listen_packets(iface):
    scapy.sniff(iface=iface, store=False, prn=analyze_packets)
    #prn = callback function

def analyze_packets(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(Raw):
            print(packet[Raw].load)

(user_input, arguments) = get_info()
listen_packets(user_input.interface)
