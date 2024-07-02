import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments


def load_dataset(file_path, tokenizer, block_size=128):
    return TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=block_size,
        overwrite_cache=True
    )

def data_collator(tokenizer):
    return DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )

def transformes_model(model_name_):
    model_name = model_name_
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    return tokenizer, model

def train_arguments(epochs):
    training_args = TrainingArguments(
    output_dir='./results',
    overwrite_output_dir=True,
    num_train_epochs=epochs,
    per_device_train_batch_size=2,
    save_steps=10_000,
    save_total_limit=2,

)
    return training_args

def training_(model, training_args, collator, data):
    trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=collator,
    train_dataset=data,
)
    trainer.train()

def save_model_tokenizer(model, tokenizer):
    return model.save_pretrained('./fine_tuned_gpt2'), tokenizer.save_pretrained('./fine_tuned_gpt2')

def transformer_testing(input_text, tokenizer, model, text_normalization):
    input_text = text_normalization(input_text)
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    output = model.generate(input_ids, max_length=100, num_return_sequences=1)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(generated_text)