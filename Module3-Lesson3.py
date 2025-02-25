import faiss
import numpy as np
import pandas as pd

print("FAISS version:", faiss.__version__)

embeddings = np.loadtxt("embeddings.csv", delimiter=",")

print("Embeddings Shape:", embeddings.shape)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("Number of vectors in the index:", index.ntotal)

query_vector = embeddings[0].reshape(1, -1)

k = 5
distances, indices = index.search(query_vector, k)

print("Distances:", distances)
print("Indices:", indices)

nlist = 50 
quantizer = faiss.IndexFlatL2(dimension)
ivf_index = faiss.IndexIVFFlat(quantizer, dimension, nlist)

ivf_index.train(embeddings)
ivf_index.add(embeddings)

distances, indices = ivf_index.search(query_vector, k)

print("Distances:", distances)
print("Indices:", indices)

faiss.write_index(index, "vector_index.faiss")

loaded_index = faiss.read_index("vector_index.faiss")

print("Vectors in reloaded index:", loaded_index.ntotal)

# metadata = pd.read_csv("metadata.csv")

# print("Closest Neighbors:")
# for i in indices[0]:
#     print(metadata.iloc[i])

