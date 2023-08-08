import os
from scapy.all import *
import json
from collections import defaultdict
from tqdm import tqdm

def packet_to_dict(packet):
    # Convert the packet to a dictionary representation
    packet_dict = {
        'source': packet[IP].src,
        'destination': packet[IP].dst,
        'sport': packet[TCP].sport,
        'dport': packet[TCP].dport,
        'flags': packet[TCP].flags,
        'seq': packet[TCP].seq,
        'ack': packet[TCP].ack,
    }
    return packet_dict

def save_tcp_packets_from_pcap(input_file):
    # Read the pcap file
    packets = rdpcap(input_file)

    # Create a list to hold the packet dictionaries
    packet_list = []

    # Save each TCP packet as a dictionary
    for packet in tqdm(packets, desc="Processing packets", unit="packet"):
        if packet.haslayer(TCP) and packet.haslayer(IP):
            packet_dict = packet_to_dict(packet)
            packet_list.append(packet_dict)

    # Create the output folder if it doesn't exist
    output_folder = "pcap_output"
    os.makedirs(output_folder, exist_ok=True)

    # Save the packets as a JSON file
    output_file = os.path.join(output_folder, 'tcp_packets.json')

    with open(output_file, 'w') as f:
        json.dump(packet_list, f, indent=4, default=str)

# Call the function with the input pcap file name
save_tcp_packets_from_pcap('Pcap Files/202004080800.pcap')
