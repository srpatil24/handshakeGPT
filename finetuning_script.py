from huggingface_hub import notebook_login
from datasets import Dataset
# notebook_login()

from datasets import load_dataset

import pandas as pd


model_name = "meta-llama/Llama-2-13b-hf"
dataset_name = 'something.csv'

output_dir = "./results"
per_device_train_batch_size = 12
gradient_accumulation_steps = 12
optim = "paged_adamw_32bit"
save_steps = None
logging_steps = 10
learning_rate = 2e-4
max_grad_norm = 0.3
max_steps = None
warmup_ratio = 0.03
lr_scheduler_type = "constant"
epoch = 1

max_seq_length = 1024


df = pd.read_csv(dataset_name)
dataset = Dataset.from_pandas(df)

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, AutoTokenizer

model_name = "meta-llama/Llama-2-13b-hf"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    trust_remote_code=True
)
model.config.use_cache = False

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token

from peft import LoraConfig, get_peft_model

lora_alpha = 16
lora_dropout = 0.1
lora_r = 64

peft_config = LoraConfig(
    lora_alpha=lora_alpha,
    lora_dropout=lora_dropout,
    r=lora_r,
    bias="none",
    task_type="CAUSAL_LM"
)

from transformers import TrainingArguments

training_arguments = TrainingArguments(
    output_dir=output_dir,
    per_device_train_batch_size=per_device_train_batch_size,
    gradient_accumulation_steps=gradient_accumulation_steps,
    optim=optim,
    report_to="wandb",
    logging_steps=logging_steps,
    learning_rate=learning_rate,
    fp16=True,
    max_grad_norm=max_grad_norm,
    warmup_ratio=warmup_ratio,
    group_by_length=True,
    num_train_epochs=epoch,
    lr_scheduler_type=lr_scheduler_type,
)

from trl import SFTTrainer



trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    peft_config=peft_config,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    tokenizer=tokenizer,
    args=training_arguments,
)

for name, module in trainer.model.named_modules():
    if "norm" in name:
        module = module.to(torch.float32)

trainer.train()

model_to_save = trainer.model.module if hasattr(trainer.model, 'module') else trainer.model  # Take care of distributed/parallel training
model_to_save.save_pretrained("outputs")

from transformers import AutoModelForCausalLM, PretrainedConfig
import torch

model = AutoModelForCausalLM.from_pretrained(model_name, device_map={"":0}, trust_remote_code=True, torch_dtype=torch.float16)

from peft import PeftModel

# load perf model with new adapters
model = PeftModel.from_pretrained(
    model,
    model_to_save,
)

print("Merging...")

model = model.merge_and_unload() # merge adapters with

print("Saving Final Merged Model")

model.save_pretrained("llama-13b-tcp")

from transformers import AutoTokenizer

print("Saving Tokenizer")

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.save_pretrained("llama-13b-tcp")

