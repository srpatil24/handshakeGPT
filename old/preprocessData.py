import json
import random

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def convert_to_list_of_dicts(data):
    # If the data is already a list of dictionaries, return it as is.
    if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        return data

    # If the data is a single dictionary, convert it to a list containing the dictionary.
    if isinstance(data, dict):
        return [data]

    # If the data is a single JSON object (e.g., not wrapped in square brackets),
    # wrap it in a list and return.
    return [data]

def create_input_output_pairs(data, sequence_length=10):
    input_output_pairs = []
    num_rows = len(data)
    for i in range(num_rows - sequence_length):
        input_sequence = data[i:i+sequence_length]
        output_row = data[i+sequence_length]
        input_output_pairs.append((input_sequence, output_row))
    return input_output_pairs

def save_preprocessed_data(input_output_pairs, output_file_path):
    with open(output_file_path, 'w') as file:
        json.dump(input_output_pairs, file, indent=2)

def main():
    json_file_path = 'pcap_output/tcp_packets_2.json'  # Replace with the actual path to your JSON file
    output_file_path = 'preprocessed_data.json'  # Replace with the desired output file path

    # Read the JSON file and convert the data to a list of dictionaries.
    data = read_json_file(json_file_path)
    data = convert_to_list_of_dicts(data)
    
    # Shuffle the input-output pairs to ensure randomness during training.
    input_output_pairs = create_input_output_pairs(data)
    random.shuffle(input_output_pairs)

    # Save the preprocessed data to a new JSON file
    save_preprocessed_data(input_output_pairs, output_file_path)

if __name__ == "__main__":
    main()
