

def build_lps(pat, lps):
    length_of_prefix = 0
    m = len(pat)
    lps[0] = 0

    i=1
    while i<m:
        if pat[i] == pat[length_of_prefix]:
            length_of_prefix += 1
            lps[i] = length_of_prefix
            i += 1

        else:
            if length_of_prefix != 0:
                length_of_prefix = lps[length_of_prefix - 1]
            else:
                lps[i] = 0
                i += 1

def search(txt, pat):
    n = len(txt)
    m = len(pat)

    lps = [0] * m
    res = []

    build_lps(pat,lps)
    i = 0
    j = 0

    while i<n:
        if txt[i] == pat[j]:
            i+=1
            j+=1
            if j == m:
                res.append(i-j)
                j = lps[j - 1]

        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return res

if __name__ == "__main__":
    txt = "aabaacaadaabaaba"
    pat = "aaba"
    res = search(txt,pat)
    for i in range(len(res)):
        print(res[i], end=" ")


