from transformers import GPT2LMHeadModel, GPT2Tokenizer
import sys

# Load pre-trained model and tokenizer
model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Prepare the input prompt
prompt = " ".join(sys.argv[1:])
inputs = tokenizer.encode(prompt, return_tensors='pt')

# Generate text
outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(text)
