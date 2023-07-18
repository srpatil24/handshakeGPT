import os
from scapy.all import *
import json
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

    print("FINISHED READING THE PCAP, NOW STARTING TO DUMPT TO JSON")
    # Create the output folder if it doesn't exist
    output_folder = "pcap_output"
    os.makedirs(output_folder, exist_ok=True)

    # Save the packets as a JSON file
    output_file = os.path.join(output_folder, 'tcp_packets.json')

    with open(output_file, 'w') as f:
        for packet in tqdm(packets, desc="Processing packets", unit="packet"):
            if packet.haslayer(TCP) and packet.haslayer(IP):
                packet_dict = packet_to_dict(packet)
                json.dump(packet_dict, f, default=str)
                f.write('\n')

save_tcp_packets_from_pcap('Pcap Files/202004080800.pcap')
