import json

# Read the JSON file
input_file_path = 'output_predictions_test_4.json'
output_file_path = 'reformated_check.json'

def extract_tcp_packet(packet_text):
    start_index = packet_text.find("Answer:\n")
    end_index = packet_text.find("}", start_index)
    if start_index != -1 and end_index != -1:
        extracted_text = packet_text[start_index + len("Answer:\n"):end_index + 1]
        extracted_text = extracted_text.replace("'", "\"")  # Replace single quotes with double quotes
        return json.loads(extracted_text)
    return None

with open(input_file_path, 'r') as input_file:
    data = json.load(input_file)

# Process and modify the entries
for entry_key, entry_values in data.items():
    new_entries = []
    for entry in entry_values:
        if 'Predicted_TCP_Packet' in entry:
            predicted_tcp_packet = entry['Predicted_TCP_Packet']
            parsed_packet = extract_tcp_packet(predicted_tcp_packet)
            if parsed_packet:
                entry['Predicted_TCP_Packet'] = parsed_packet
                new_entries.append(entry)
    data[entry_key] = new_entries

# Write the modified data to a new JSON file
with open(output_file_path, 'w') as output_file:
    json.dump(data, output_file, indent=4)

print("File processing complete.")
