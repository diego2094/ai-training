import pandas as pd
import openai
from transformers import AutoTokenizer, AutoModel
import torch


file_path = "employees_cleaned.csv"
df = pd.read_csv(file_path)

print("Dataset Preview:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nUnique Roles:")
print(df['Role'].unique())

print("\nNumber of Departments:")
print(df['Department'].nunique())

# Generate embeddings with OpenAI

text = "Software Engineer in the AI Department"

client = openai.OpenAI()

response = client.embeddings.create(
    input=text,
    model="text-embedding-ada-002"
)
embedding = response['data'][0]['embedding']

print("\nGenerated Embedding:")
print(embedding[:10])

# Generate embeddings with HuggingFace Transformers

model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

text = "Software Engineer in the AI Department"

tokens = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    output = model(**tokens)
    embedding = output.last_hidden_state.mean(dim=1).squeeze()

print("\nGenerated Embedding:")
print(embedding[:10]) 
