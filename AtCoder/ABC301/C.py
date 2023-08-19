from collections import defaultdict
from string import ascii_lowercase

S = input()
T = input()

CS = defaultdict(int)
CT = defaultdict(int)

for c in S:
    CS[c] += 1
for c in T:
    CT[c] += 1

for c in ascii_lowercase:
    if c in "atcoder":
        s = CS[c]
        t = CT[c]
        if s < t:
            CS["@"] -= t - s
        else:
            CT["@"] -= s - t

    else:
        if CS[c] != CT[c]:
            print("No")
            exit()

if CS["@"] < 0 or CT["@"] < 0:
    print("No")
    exit()


print("Yes")
