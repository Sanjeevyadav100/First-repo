import numpy as np
from multiprocessing import Pool

def dot_product_chunk(args):
    a_chunk, b_chunk = args
    return np.dot(a_chunk, b_chunk)

def parallel_dot_product(a, b, num_chunks=4):
    # Split the vectors into chunks
    chunk_size = len(a) // num_chunks
    chunks = [(a[i:i + chunk_size], b[i:i + chunk_size]) for i in range(0, len(a), chunk_size)]

    with Pool(processes=num_chunks) as pool:
        # Calculate dot products for each chunk in parallel
        results = pool.map(dot_product_chunk, chunks)

    # Sum the results from each chunk
    return sum(results)

if __name__ == "__main__":
    # Example usage
    size = 1_000_000
    a = np.random.rand(size)
    b = np.random.rand(size)

    result = parallel_dot_product(a, b)
    print("Dot product:", result)

