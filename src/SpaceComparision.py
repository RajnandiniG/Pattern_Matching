import sys  # For memory usage measurement

# Function to compute the LPS array for KMP
def compute_lps_space(pattern):
    m = len(pattern)
    lps = [0] * m  # LPS array
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

    # Return the LPS array and its size
    return lps, sys.getsizeof(lps)


# Function to calculate Rabin-Karp's hash values
def rabin_karp_hash_space(pattern, text, prime=101):
    m = len(pattern)
    n = len(text)
    pattern_hash = 0
    current_hash = 0
    h = 1

    # Precompute h = pow(prime, m-1)
    for _ in range(m - 1):
        h = (h * prime)

    # Compute initial hash values
    for i in range(m):
        pattern_hash = (prime * pattern_hash + ord(pattern[i]))
        current_hash = (prime * current_hash + ord(text[i]))

    # Memory usage: two hashes (pattern + sliding hash) + scalar value h
    space_used = sys.getsizeof(pattern_hash) + sys.getsizeof(current_hash) + sys.getsizeof(h)
    return space_used


# Space Comparison Function
def compare_space_requirements(patterns, text):
    print("== Space Requirements ==")
    for pattern in patterns:
        print(f"\nPattern: {pattern}")
        # KMP Space
        lps, kmp_space = compute_lps_space(pattern)
        print(f"LPS Array (KMP): {lps}")
        print(f"Space Used by LPS Array: {kmp_space} bytes")

        # Rabin-Karp Space
        rk_space = rabin_karp_hash_space(pattern, text)
        print(f"Space Used by Hash Values (Rabin-Karp): {rk_space} bytes")

        # Conclusion
        print("\nComparison:")
        if kmp_space > rk_space:
            print(f"KMP uses more memory ({kmp_space} bytes) than Rabin-Karp ({rk_space} bytes).")
        elif kmp_space < rk_space:
            print(f"Rabin-Karp uses more memory ({rk_space} bytes) than KMP ({kmp_space} bytes).")
        else:
            print(f"Both algorithms use the same amount of memory ({kmp_space} bytes).")


# Main Function for Tests
if __name__ == "__main__":
    # Example Input
    text = "aabaacaadaabaaba"
    patterns = ["aaba", "aca"]

    # Compare Space Requirements
    compare_space_requirements(patterns, text)

    # Test with Larger Patterns
    print("\n== Large Pattern Test ==")
    text = "a" * 10000 + "b"
    patterns = ["a" * 100, "a" * 200, "a" * 500]
    compare_space_requirements(patterns, text)
