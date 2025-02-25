import pandas as pd
from transformers import AutoTokenizer, AutoModel, pipeline
import torch
import faiss
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
# import openai

data_path = "jarvid_profiles.csv"
df = pd.read_csv(data_path)

print("Dataset Preview:")
print(df)

# def generate_embedding(text):
#     response = openai.Embedding.create(
#         input=text,
#         model="text-embedding-ada-002"
#     )
#     return response['data'][0]['embedding']

# # Combine employee data into a single string and generate embeddings
# df['profile'] = df['Name'] + " is a " + df['Role'] + " in " + df['Department']
# df['embedding'] = df['profile'].apply(generate_embedding)

# print("Embeddings generated successfully!")


model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def generate_embedding(text):
    tokens = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        output = model(**tokens)
    return output.last_hidden_state.mean(dim=1).squeeze().numpy()

df['profile'] = df['Name'] + " is a " + df['Role'] + " in " + df['Department']
df['embedding'] = df['profile'].apply(generate_embedding)

print("Embeddings generated successfully!")

embeddings = np.array(df['embedding'].tolist())

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)
print(f"Number of vectors in the index: {index.ntotal}")

query = "Find an expert in AI development."

query_embedding = generate_embedding(query)

k = 3  
distances, indices = index.search(np.array([query_embedding]), k)

print("Retrieved Profiles:")
for idx in indices[0]:
    print(df.iloc[idx]['profile'])

context = "\n".join(df.iloc[idx]['profile'] for idx in indices[0])

final_prompt = f"Context: {context}\n\nQuery: {query}\n\nAnswer:"

generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

response = generator(final_prompt, max_length=100)

print("Generated Response:")
print(response[0]["generated_text"])

pca = PCA(n_components=2)
reduced_embeddings = pca.fit_transform(embeddings)
reduced_query = pca.transform([query_embedding])

plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], label="Employee Profiles", color='blue')
plt.scatter(reduced_query[:, 0], reduced_query[:, 1], label="Query", color='red')
plt.legend()
plt.title("Embedding Space Visualization")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.show()
