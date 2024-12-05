import time

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

# Rabin-Karp Preprocessing: Compute Hashes
def compute_hash(pattern, prime=101):
    hash_value = 0
    for i, char in enumerate(pattern):
        hash_value += ord(char) * (prime ** i)
    return hash_value

# Measure Preprocessing Time
def measure_preprocessing(single_pattern, multiple_patterns):
    print("== Measuring Preprocessing Overhead ==")

    # KMP Preprocessing
    print("\nKMP Algorithm:")
    start_time = time.perf_counter()
    lps_single = compute_lps(single_pattern)
    kmp_single_time = time.perf_counter() - start_time
    print(f"Single Pattern LPS Time: {kmp_single_time:.6f} seconds")

    start_time = time.perf_counter()
    lps_multiple = [compute_lps(p) for p in multiple_patterns]
    kmp_multiple_time = time.perf_counter() - start_time
    print(f"Multiple Patterns LPS Time: {kmp_multiple_time:.6f} seconds")

    # Rabin-Karp Preprocessing
    print("\nRabin-Karp Algorithm:")
    start_time = time.perf_counter()
    hash_single = compute_hash(single_pattern)
    rk_single_time = time.perf_counter() - start_time
    print(f"Single Pattern Hash Time: {rk_single_time:.6f} seconds")

    start_time = time.perf_counter()
    hashes_multiple = [compute_hash(p) for p in multiple_patterns]
    rk_multiple_time = time.perf_counter() - start_time
    print(f"Multiple Patterns Hash Time: {rk_multiple_time:.6f} seconds")

single_pattern = "aabaacaadaabaaba"
multiple_patterns = ["aaba", "abac", "aaaa", "baba", "abab"]

measure_preprocessing(single_pattern, multiple_patterns)
