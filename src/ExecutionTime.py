import time  # For measuring execution time

# Rabin-Karp Algorithm with Time and Character Comparison Count
def rabin_karp_with_comparisons(pattern, text, prime=101):
    m, n = len(pattern), len(text)
    pattern_hash = 0
    current_hash = 0
    h = 1
    comparison_count = 0  # Counter for comparisons
    matches = []

    # Precompute h = pow(prime, m-1)
    for _ in range(m - 1):
        h = (h * prime)

    # Compute initial hash values
    for i in range(m):
        pattern_hash = (prime * pattern_hash + ord(pattern[i]))
        current_hash = (prime * current_hash + ord(text[i]))

    # Slide the pattern over the text
    for i in range(n - m + 1):
        # Compare hashes
        comparison_count += 1  # One comparison for hashes
        if pattern_hash == current_hash:
            # Check characters one-by-one
            for j in range(m):
                comparison_count += 1  # Increment for each character comparison
                if text[i + j] != pattern[j]:
                    break
            else:
                matches.append(i)

        # Compute the next hash
        if i < n - m:
            current_hash = (prime * (current_hash - ord(text[i]) * h) + ord(text[i + m]))

    return matches, comparison_count


# KMP Algorithm with Time and Character Comparison Count
def kmp_with_comparisons(pattern, text):
    lps = compute_lps_with_comparisons(pattern)
    m, n = len(pattern), len(text)
    i, j = 0, 0
    comparison_count = 0  # Counter for comparisons
    matches = []

    while i < n:
        comparison_count += 1  # Increment for every character comparison
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparison_count


# LPS Array Calculation for KMP with Comparison Count
def compute_lps_with_comparisons(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    comparison_count = 0  # Counter for LPS character comparisons

    while i < m:
        comparison_count += 1  # Increment for each character comparison
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


# Comparison Test Function with Timing
def compare_algorithms_with_timing(patterns, text):
    print(f"Text Length: {len(text)}")
    print(f"Text: {text}")
    print(f"Patterns: {patterns}")

    for pattern in patterns:
        print(f"\nPattern: {pattern}")
        # Run Rabin-Karp
        start_time = time.time()
        rk_matches, rk_comparisons = rabin_karp_with_comparisons(pattern, text)
        rk_time = time.time() - start_time

        print("\nRabin-Karp Results:")
        print(f"Matches: {rk_matches}")
        print(f"Character Comparisons: {rk_comparisons}")
        print(f"Execution Time: {rk_time:.6f} seconds")

        # Run KMP
        start_time = time.time()
        kmp_matches, kmp_comparisons = kmp_with_comparisons(pattern, text)
        kmp_time = time.time() - start_time

        print("\nKMP Results:")
        print(f"Matches: {kmp_matches}")
        print(f"Character Comparisons: {kmp_comparisons}")
        print(f"Execution Time: {kmp_time:.6f} seconds")

        # Conclusion
        print("\n== Comparison Summary ==")
        print(f"Rabin-Karp Time: {rk_time:.6f} seconds, Comparisons: {rk_comparisons}")
        print(f"KMP Time: {kmp_time:.6f} seconds, Comparisons: {kmp_comparisons}")
        if rk_comparisons > kmp_comparisons:
            print("KMP is more efficient in terms of character comparisons.")
        elif rk_comparisons < kmp_comparisons:
            print("Rabin-Karp is more efficient in terms of character comparisons.")
        else:
            print("Both algorithms performed the same number of comparisons.")
        print()


# Main Function to Run Tests with Timing
if __name__ == "__main__":
    # Example Input
    text = "aabaacaadaabaaba"
    patterns = ["aaba", "aca"]

    print("== Example Test ==")
    compare_algorithms_with_timing(patterns, text)

    # Large Input Test
    print("== Large Input Test ==")
    text = "a" * 10000 + "b"
    patterns = ["aaa", "aaaa", "aaaaa"]
    compare_algorithms_with_timing(patterns, text)
