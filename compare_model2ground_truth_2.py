import json


input_file_path = '/home/brett/test_model/test/flattened_conversations.json'
output_file = 'check_accuracy.json'

def extract_source(input_file_path):
    extracted_source = []

    with open(input_file_path, 'r') as f:
        data = json.load(f)

    for entry in data:
        if 'Predicted_TCP_Packet' in entry and 'source' in entry[
            'Predicted_TCP_Packet']:  # ('Predicted_TCP_Packet' in entry and 'flags' in entry['Predicted_TCP_Packet']) or ('Correct_Answer' in entry and 'flags' in entry['Correct_Answer']):
            source = entry['Predicted_TCP_Packet']['source']
            if isinstance(source, str):
                extracted_source.append(source)
            elif isinstance(source, list):
                extracted_source.extend(source)
        if 'Correct_Answer' in entry and 'source' in entry['Correct_Answer']:
            source = entry['Correct_Answer']['source']
            if isinstance(source, str):
                extracted_source.append(source)
            elif isinstance(source, list):
                extracted_source.extend(source)

    # Group the flags into pairs: 1-2, 3-4, 5-6
    source_source = [extracted_source[i:i + 2] for i in range(0, len(extracted_source), 2)]

    # Calculate the percentage of matching pairs
    total_source = len(source_source)
    matching_source = sum(1 for pair in source_source if pair[0] == pair[1])
    percentage_matching = (matching_source / total_source) * 100

    return percentage_matching

def extract_destination(input_file_path):
    extracted_destination = []

    with open(input_file_path, 'r') as f:
        data = json.load(f)

    for entry in data:
        if 'Predicted_TCP_Packet' in entry and 'destination' in entry[
            'Predicted_TCP_Packet']:  # ('Predicted_TCP_Packet' in entry and 'flags' in entry['Predicted_TCP_Packet']) or ('Correct_Answer' in entry and 'flags' in entry['Correct_Answer']):
            destination = entry['Predicted_TCP_Packet']['destination']
            if isinstance(destination, str):
                extracted_destination.append(destination)
            elif isinstance(destination, list):
                extracted_destination.extend(destination)
        if 'Correct_Answer' in entry and 'destination' in entry['Correct_Answer']:
            destination = entry['Correct_Answer']['destination']
            if isinstance(destination, str):
                extracted_destination.append(destination)
            elif isinstance(destination, list):
                extracted_destination.extend(destination)

    # Group the flags into pairs: 1-2, 3-4, 5-6
    destination_pairs = [extracted_destination[i:i + 2] for i in range(0, len(extracted_destination), 2)]

    # Calculate the percentage of matching pairs
    total_pairs = len(destination_pairs)
    matching_pairs = sum(1 for pair in destination_pairs if pair[0] == pair[1])
    percentage_matching = (matching_pairs / total_pairs) * 100

    return percentage_matching


def extract_sport(input_file_path):
    extracted_sport = []

    with open(input_file_path, 'r') as f:
        data = json.load(f)

    for entry in data:
        if 'Predicted_TCP_Packet' in entry and 'sport' in entry[
            'Predicted_TCP_Packet']:  # ('Predicted_TCP_Packet' in entry and 'flags' in entry['Predicted_TCP_Packet']) or ('Correct_Answer' in entry and 'flags' in entry['Correct_Answer']):
            sport = entry['Predicted_TCP_Packet']['sport']
            if isinstance(sport, int):
                extracted_sport.append(sport)
            elif isinstance(sport, list):
                extracted_sport.extend(sport)
        if 'Correct_Answer' in entry and 'sport' in entry['Correct_Answer']:
            sport = entry['Correct_Answer']['sport']
            if isinstance(sport, int):
                extracted_sport.append(sport)
            elif isinstance(sport, list):
                extracted_sport.extend(sport)

    # Group the flags into pairs: 1-2, 3-4, 5-6
    sport_pairs = [extracted_sport[i:i + 2] for i in range(0, len(extracted_sport), 2)]

    # Calculate the percentage of matching pairs
    total_pairs = len(sport_pairs)
    matching_pairs = sum(1 for pair in sport_pairs if pair[0] == pair[1])
    percentage_matching = (matching_pairs / total_pairs) * 100

    return percentage_matching

def extract_dport(input_file_path):
    extracted_dport = []

    with open(input_file_path, 'r') as f:
        data = json.load(f)

    for entry in data:
        if 'Predicted_TCP_Packet' in entry and 'dport' in entry[
            'Predicted_TCP_Packet']:  # ('Predicted_TCP_Packet' in entry and 'flags' in entry['Predicted_TCP_Packet']) or ('Correct_Answer' in entry and 'flags' in entry['Correct_Answer']):
            dport = entry['Predicted_TCP_Packet']['dport']
            if isinstance(dport, int):
                extracted_dport.append(dport)
            elif isinstance(dport, list):
                extracted_dport.extend(dport)
        if 'Correct_Answer' in entry and 'dport' in entry['Correct_Answer']:
            dport = entry['Correct_Answer']['dport']
            if isinstance(dport, int):
                extracted_dport.append(dport)
            elif isinstance(dport, list):
                extracted_dport.extend(dport)

    # Group the flags into pairs: 1-2, 3-4, 5-6
    dport_pairs = [extracted_dport[i:i + 2] for i in range(0, len(extracted_dport), 2)]

    # Calculate the percentage of matching pairs
    total_pairs = len(dport_pairs)
    matching_pairs = sum(1 for pair in dport_pairs if pair[0] == pair[1])
    percentage_matching = (matching_pairs / total_pairs) * 100

    return percentage_matching

def extract_flags(input_file_path):
    extracted_flags = []

    with open(input_file_path, 'r') as f:
        data = json.load(f)

    for entry in data:
        if 'Predicted_TCP_Packet' in entry and 'flags' in entry[
            'Predicted_TCP_Packet']:  # ('Predicted_TCP_Packet' in entry and 'flags' in entry['Predicted_TCP_Packet']) or ('Correct_Answer' in entry and 'flags' in entry['Correct_Answer']):
            flags = entry['Predicted_TCP_Packet']['flags']
            if isinstance(flags, str):
                extracted_flags.append(flags)
            elif isinstance(flags, list):
                extracted_flags.extend(flags)
        if 'Correct_Answer' in entry and 'flags' in entry['Correct_Answer']:
            flags = entry['Correct_Answer']['flags']
            if isinstance(flags, str):
                extracted_flags.append(flags)
            elif isinstance(flags, list):
                extracted_flags.extend(flags)

    # Group the flags into pairs: 1-2, 3-4, 5-6
    flag_pairs = [extracted_flags[i:i + 2] for i in range(0, len(extracted_flags), 2)]

    # Calculate the percentage of matching pairs
    total_pairs = len(flag_pairs)
    matching_pairs = sum(1 for pair in flag_pairs if pair[0] == pair[1])
    percentage_matching = (matching_pairs / total_pairs) * 100

    return percentage_matching

def extract_seq(input_file_path):
    extracted_seq = []

    with open(input_file_path, 'r') as f:
        data = json.load(f)

    for entry in data:
        if 'Predicted_TCP_Packet' in entry and 'seq' in entry[
            'Predicted_TCP_Packet']:  # ('Predicted_TCP_Packet' in entry and 'flags' in entry['Predicted_TCP_Packet']) or ('Correct_Answer' in entry and 'flags' in entry['Correct_Answer']):
            seq = entry['Predicted_TCP_Packet']['seq']
            if isinstance(seq, int):
                extracted_seq.append(seq)
            elif isinstance(seq, list):
                extracted_seq.extend(seq)
        if 'Correct_Answer' in entry and 'seq' in entry['Correct_Answer']:
            seq = entry['Correct_Answer']['seq']
            if isinstance(seq, int):
                extracted_seq.append(seq)
            elif isinstance(seq, list):
                extracted_seq.extend(seq)

    # Group the flags into pairs: 1-2, 3-4, 5-6
    seq_pairs = [extracted_seq[i:i + 2] for i in range(0, len(extracted_seq), 2)]

    # Calculate the percentage of matching pairs
    total_pairs = len(seq_pairs)
    matching_pairs = sum(1 for pair in seq_pairs if pair[0] == pair[1])
    percentage_matching = (matching_pairs / total_pairs) * 100

    return percentage_matching

def extract_ack(input_file_path):
    extracted_ack = []

    with open(input_file_path, 'r') as f:
        data = json.load(f)

    for entry in data:
        if 'Predicted_TCP_Packet' in entry and 'ack' in entry[
            'Predicted_TCP_Packet']:  # ('Predicted_TCP_Packet' in entry and 'flags' in entry['Predicted_TCP_Packet']) or ('Correct_Answer' in entry and 'flags' in entry['Correct_Answer']):
            ack = entry['Predicted_TCP_Packet']['ack']
            if isinstance(ack, int):
                extracted_ack.append(ack)
            elif isinstance(ack, list):
                extracted_ack.extend(ack)
        if 'Correct_Answer' in entry and 'ack' in entry['Correct_Answer']:
            ack = entry['Correct_Answer']['ack']
            if isinstance(ack, int):
                extracted_ack.append(ack)
            elif isinstance(ack, list):
                extracted_ack.extend(ack)

    # Group the flags into pairs: 1-2, 3-4, 5-6
    ack_pairs = [extracted_ack[i:i + 2] for i in range(0, len(extracted_ack), 2)]

    # Calculate the percentage of matching pairs
    total_pairs = len(ack_pairs)
    matching_pairs = sum(1 for pair in ack_pairs if pair[0] == pair[1])
    percentage_matching = (matching_pairs / total_pairs) * 100

    return percentage_matching


source_string = extract_source(input_file_path)
destination_string = extract_destination(input_file_path)
sport_string = extract_sport(input_file_path)
dport_string = extract_dport(input_file_path)
flag_string = extract_flags(input_file_path)
seq_string = extract_seq(input_file_path)
ack_string = extract_ack(input_file_path)

print("source: ", source_string, "%")
print("destination: ", destination_string, "%")
print("sport: ", sport_string, "%")
print("dport: ", dport_string, "%")
print("flags: ", flag_string, "%")
print("seq: ", seq_string, "%")
print("ack: ", ack_string, "%")
