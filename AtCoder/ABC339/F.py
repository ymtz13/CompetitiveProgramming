from collections import defaultdict

N = int(input())
A = [int(input()) for _ in range(N)]
D = defaultdict(int)
for a in A:
    D[a] += 1

ans = 0
for i, ai in enumerate(A):
    for j, aj in enumerate(A[i:], i):
        p = ai * aj
        if p in D:
            ans += D[p] * (1 if i == j else 2)

print(ans)
