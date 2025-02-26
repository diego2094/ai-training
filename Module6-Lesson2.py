import numpy as np
import faiss
import time

dimension = 128
num_embeddings = 1000000
embeddings = np.random.random((num_embeddings, dimension)).astype('float32')

np.save("embeddings.npy", embeddings)

embeddings = np.load("embeddings.npy")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)


def measure_latency(query_vector, k=10):
    start = time.perf_counter()
    distances, indices = index.search(query_vector, k)
    end = time.perf_counter()
    latency = (end - start) * 1000 
    return latency, indices

query_vector = np.random.random((1, embeddings.shape[1])).astype('float32')

latency, results = measure_latency(query_vector)
print(f"Latency: {latency:.2f} ms")

for n_queries in [1, 10, 100]:
    query_vectors = np.random.random((n_queries, embeddings.shape[1])).astype('float32')
    latency, _ = measure_latency(query_vectors)
    print(f"Latency for {n_queries} queries: {latency:.2f} ms")

num_clusters = 100  
quantizer = faiss.IndexFlatL2(dimension)
ivf_index = faiss.IndexIVFFlat(quantizer, dimension, num_clusters)

ivf_index.train(embeddings)
ivf_index.add(embeddings)

ivf_index.nprobe = 10  

def compare_performance(query_vector):
    start_flat = time.perf_counter()
    _, flat_results = index.search(query_vector, 10)
    end_flat = time.perf_counter()

    start_ivf = time.perf_counter()
    _, ivf_results = ivf_index.search(query_vector, 10)
    end_ivf = time.perf_counter()

    print(f"FlatL2 Latency: {(end_flat - start_flat) * 1000:.2f} ms")
    print(f"IVF Latency: {(end_ivf - start_ivf) * 1000:.2f} ms")

compare_performance(query_vector)

pq_index = faiss.IndexPQ(dimension, 8, 8) 
pq_index.train(embeddings)
pq_index.add(embeddings)

def measure_pq_latency(query_vector):
    start = time.perf_counter()
    _, pq_results = pq_index.search(query_vector, 10)
    end = time.perf_counter()
    print(f"PQ Latency: {(end - start) * 1000:.2f} ms")

measure_pq_latency(query_vector)

for nprobe in [1, 5, 10, 20]:
    ivf_index.nprobe = nprobe
    latency, _ = measure_latency(query_vector)
    print(f"nprobe={nprobe}, Latency: {latency:.2f} ms")
