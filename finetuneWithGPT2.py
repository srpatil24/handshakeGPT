import pandas as pd
from transformers import GPT2Tokenizer, GPT2LMHeadModel, GPT2Config, AdamW
import torch
from torch.utils.data import DataLoader, TensorDataset, random_split
import json

# Load the DataFrame and create a column 'input_sequence' containing the previous 10 rows as a list of dictionaries
def create_input_sequence(df, sequence_length=10):
    input_sequence = []
    for i in range(len(df) - sequence_length):
        input_sequence.append(df.iloc[i:i+sequence_length].to_dict('records'))
    return input_sequence

# Prepare the model inputs and labels
def prepare_inputs_labels(df, tokenizer, max_length=1024, sequence_length=10):
    input_ids = []
    labels = []

    input_sequence = create_input_sequence(df, sequence_length)

    for input_seq, output_row in zip(input_sequence, df.iloc[sequence_length:]['output'].tolist()):
        input_text = json.dumps(input_seq)
        output_text = json.dumps(output_row)

        input_tokens = tokenizer(input_text, add_special_tokens=True, truncation=True, max_length=max_length, padding='max_length')
        label_tokens = tokenizer(output_text, add_special_tokens=False, truncation=True, max_length=max_length, padding='max_length')

        input_ids.append(input_tokens['input_ids'])
        labels.append(label_tokens['input_ids'])

    return input_ids, labels

# Load the DataFrame from your source
df = pd.read_json('data/preprocessed_data.json')  # Replace with the actual path to your DataFrame

# Define the tokenizer and load the pre-trained GPT-2 model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2", config=GPT2Config.from_pretrained("gpt2"))

# Prepare the inputs and labels
input_ids, labels = prepare_inputs_labels(df, tokenizer)

# Convert to PyTorch DataLoader
input_ids = torch.tensor(input_ids)
labels = torch.tensor(labels)

dataset = TensorDataset(input_ids, labels)
train_size = 632000
train_dataset, val_dataset = random_split(dataset, [train_size, len(dataset) - train_size])

train_loader = DataLoader(train_dataset, batch_size=2, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=2)

# Fine-tuning settings
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
optimizer = AdamW(model.parameters(), lr=5e-5)

# Training loop
model.train()
for epoch in range(10):  # You can adjust the number of epochs based on your dataset size and training requirements.
    for input_batch, label_batch in train_loader:
        input_batch, label_batch = input_batch.to(device), label_batch.to(device)
        outputs = model(input_batch, labels=label_batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

# Save the fine-tuned model
model.save_pretrained('fine_tuned_gpt2_model')
tokenizer.save_pretrained('fine_tuned_gpt2_model')