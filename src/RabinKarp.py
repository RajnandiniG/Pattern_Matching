
d = 256
def rabin(pat, txt, q):
     m = len(pat)
     n = len(txt)
     i = 0
     j = 0
     p = 0
     t = 0
     h = 1

     for i in range(m-1):
         h = (h*d) % q

     for i in range(m):
         p = (d*p + ord(pat[i])) % q
         t = (d*t + ord(txt[i])) % q

     for i in range(n-m+1):
         if p == t:
             for i in range(m):
                 if txt[i+j] != pat[j]:
                     break
                 else:
                     j += 1
             if j == m:
                 print("Pattern found at index" + str(i))
         if i < n-m:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+m])) % q
            if t < 0:
                t += q


if __name__ == '__main__':
    txt = "aabaacaadaabaaba"
    pat = "aaba"
    q = 101
    rabin(pat, txt, q)