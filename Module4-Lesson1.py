import pandas as pd
from transformers import pipeline
import faiss
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import openai

data_path = "jarvid_profiles.csv"
df = pd.read_csv(data_path)

print("Dataset Preview:")
print(df)

client = openai.OpenAI()

def generate_embedding(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

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

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": final_prompt}
    ],
    max_tokens=100
)

print("Generated Response:")
print(response.choices[0].message.content)

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
