from collections import defaultdict


def factorize(X):
    f = defaultdict(int)
    for p in range(2, X + 1):
        if p * p > X:
            break
        while X % p == 0:
            X //= p
            f[p] += 1

    if X > 1:
        f[X] += 1

    return f


N = int(input())
A = list(map(int, input().split()))

X = defaultdict(int)
n0 = 0
ans = 0
for i, a in enumerate(A):
    if a == 0:
        ans += i
        n0 += 1
    else:
        f = factorize(a)
        s = tuple(sorted((p for p, c in f.items() if c % 2)))

        ans += n0
        ans += X[s]
        X[s] += 1

print(ans)
