from collections import defaultdict

N = int(input())
S = input()

D = defaultdict(int)

p = ""
for c in S:
    if c != p:
        p = c
        s = 0
    s += 1
    D[c] = max(D[c], s)

print(sum(D.values()))
