import faiss
import numpy as np
import openai

profiles = [
    {"id": 1, "name": "Alice", "role": "Python Developer", "department": "AI Development"},
    {"id": 2, "name": "Bob", "role": "Data Scientist", "department": "Data Analytics"},
    {"id": 3, "name": "Carol", "role": "Backend Engineer", "department": "API Integrations"},
]

embeddings = [
    [0.1, 0.2, 0.3],  # Alice
    [0.3, 0.4, 0.5],  # Bob
    [0.5, 0.6, 0.7],  # Carol
]

embeddings_array = np.array(embeddings, dtype=np.float32)

dimension = embeddings_array.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings_array)

print(f"Number of vectors in FAISS index: {index.ntotal}")

client = openai.OpenAI()

def generate_query_embedding(query):
    response = client.embeddings.create(
        input=query,
        model="text-embedding-ada-002"
    )
    return np.array(response['data'][0]['embedding'], dtype=np.float32)

query = "Who can help me with Python development?"
query_embedding = generate_query_embedding(query)

query_embedding = query_embedding.reshape(1, -1)

k = 3

distances, indices = index.search(query_embedding, k)

print("Distances:", distances)
print("Indices:", indices)

retrieved_profiles = [profiles[idx] for idx in indices[0]]
print("Retrieved Profiles:", retrieved_profiles)

context = "\n".join([
    f"{profile['name']}, a {profile['role']} in {profile['department']}"
    for profile in retrieved_profiles
])

prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100
)

print("Generated Response:")
print(response['choices'][0]['text'].strip())
