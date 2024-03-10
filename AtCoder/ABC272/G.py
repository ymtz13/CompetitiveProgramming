from collections import defaultdict
from random import choice

N = int(input())
A = list(map(int, input().split()))

S = set()

for _ in range(50):
    a1 = choice(A)
    a2 = choice(A)
    d = a2 - a1
    if d == 0:
        continue

    if d % 4 == 0:
        S.add(4)
    while d % 2 == 0:
        d //= 2

    for p in range(3, d + 1, 2):
        if d == 1:
            break
        if p * p > d:
            S.add(d)
            break
        if d % p == 0:
            S.add(p)
        while d % p == 0:
            d //= p

for s in S:
    count = defaultdict(int)
    for a in A:
        r = a % s
        count[r] += 1

    if max(count.values()) > N // 2:
        print(s)
        exit()

print(-1)
