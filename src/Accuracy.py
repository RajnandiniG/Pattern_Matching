import time

# Rabin-Karp Algorithm
def rabin_karp_search(pattern, text, prime=3):
    m, n = len(pattern), len(text)
    pattern_hash = 0
    current_hash = 0
    h = 1
    false_positives = 0
    matches = []

    # Precompute the value of h = pow(prime, m-1) % prime
    for _ in range(m - 1):
        h = (h * prime)

    # Calculate the hash for the pattern and the first window of text
    for i in range(m):
        pattern_hash = (prime * pattern_hash + ord(pattern[i]))
        current_hash = (prime * current_hash + ord(text[i]))

    # Slide the window over the text
    for i in range(n - m + 1):
        # Check if hashes match
        if pattern_hash == current_hash:
            # Double-check by comparing the characters
            if text[i:i + m] == pattern:
                matches.append(i)
            else:
                false_positives += 1

        # Calculate the hash for the next window
        if i < n - m:
            current_hash = (prime * (current_hash - ord(text[i]) * h) + ord(text[i + m]))

    return matches, false_positives

# KMP Algorithm
def kmp_search(pattern, text):
    lps = compute_lps(pattern)
    m, n = len(pattern), len(text)
    i, j = 0, 0
    matches = []

    while i < n:
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

    return matches

# LPS Array for KMP
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

# Test Function to Compare Accuracy
def compare_accuracy(pattern, text):
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")

    # Run Rabin-Karp
    rk_matches, rk_false_positives = rabin_karp_search(pattern, text)
    print("\nRabin-Karp Results:")
    print(f"Matches: {rk_matches}")
    print(f"False Positives: {rk_false_positives}")

    # Run KMP
    kmp_matches = kmp_search(pattern, text)
    print("\nKMP Results:")
    print(f"Matches: {kmp_matches}")

    # Accuracy Comparison
    is_rk_accurate = rk_false_positives == 0
    print("\n== Accuracy Comparison ==")
    print(f"KMP is always accurate: True")
    print(f"Rabin-Karp accurate: {is_rk_accurate}")
    if not is_rk_accurate:
        print(f"Rabin-Karp had {rk_false_positives} false positives.")

# Example Input
pattern = "baba"
text = "ababababababababababbababababababababababababaababbaabbabababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababahbsidiadbabababababiasdasdbababaafiaisfbabbabababababababa"
compare_accuracy(pattern, text)
