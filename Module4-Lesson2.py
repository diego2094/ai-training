import faiss
import numpy as np
import openai

client = openai.OpenAI()

profiles = [
    {"id": 1, "name": "Alice", "role": "Python Developer", "department": "AI Development"},
    {"id": 2, "name": "Bob", "role": "Data Scientist", "department": "Data Analytics"},
    {"id": 3, "name": "Carol", "role": "Backend Engineer", "department": "API Integrations"},
]

def generate_embedding(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return np.array(response.data[0].embedding, dtype=np.float32)

profiles_text = [f"{p['name']} {p['role']} {p['department']}" for p in profiles]
embeddings = np.array([generate_embedding(text) for text in profiles_text])

dimension = embeddings.shape[1]
print(f"Embeddings dimension: {dimension}")

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print(f"Number of vectors in FAISS index: {index.ntotal}")

query = "Who can help me with Python development?"
query_embedding = generate_embedding(query).reshape(1, -1)

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

response = client.chat.completions.create( 
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=100
)

print("Generated Response:")
print(response.choices[0].message.content.strip()) 
