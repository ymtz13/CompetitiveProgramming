from collections import defaultdict
from string import ascii_lowercase

S = input()

D = defaultdict(int)
for c in S:
    D[c] += 1

m = max(D.values())

for c in ascii_lowercase:
    if D[c] == m:
        print(c)
        exit()
