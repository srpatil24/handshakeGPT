# HandshakeGPT

## Data Collection
1. Open Wireshark
2. Start Capturing Packets
3. Run the following commands in Command Prompt (or the equivalent):
```
pip3 install selenium
git clone https://github.com/srpatil24/handshakeGPT.git
cd handshakeGPT/dataCollection
python3 randomWebsites.py
```
4. After at least 30-45 minutes, stop the script and stop capturing packets
5. Save the pcap output file to the directory of the github project


## Extract Three Way Handshakes

1. cd into the directory of the github project
2. Run the following commands
```
pip3 install scapy
# replace input.pcap with the name of the PCAP file you generated earlier
# the output argument is optional
python3 extractThreeWayHandshakeDataToJson.py --input input.pcap --output output.json
```
