import pandas as pd
import openai
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

file_path = "employees_cleaned.csv"
df = pd.read_csv(file_path)

print("Dataset Preview:")
print(df.head())

assert not df[['Role', 'Department']].isnull().any().any(), "Dataset contains missing values."

# Generate embeddings with OpenAI
client = openai.OpenAI()

def generate_embedding_openai(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

df['role_embedding'] = df['Role'].apply(generate_embedding_openai)
df['department_embedding'] = df['Department'].apply(generate_embedding_openai)
print("Embeddings generated successfully!")

# Generate embeddings with HuggingFace Transformers
model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def generate_embedding_huggingFace(text):
    tokens = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        output = model(**tokens)
    return output.last_hidden_state.mean(dim=1).squeeze().numpy()

df['role_embedding'] = df['Role'].apply(generate_embedding_huggingFace)
df['department_embedding'] = df['Department'].apply(generate_embedding_huggingFace)

print("Embeddings generated successfully!")

embeddings = np.array([
    np.concatenate((role, department))
    for role, department in zip(df['role_embedding'], df['department_embedding'])
])

np.savetxt("embeddings.csv", embeddings, delimiter=",")
print("Embeddings saved to 'embeddings.csv' successfully!")
