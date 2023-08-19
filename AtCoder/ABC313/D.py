N, K = map(int, input().split())
ans = [0] * (N + 1)

Q1 = []
for k in range(1, K + 2):
    Q1.append(tuple(v for v in range(1, K + 2) if v != k))

A = []
for i, q in enumerate(Q1):
    print("?", *q)
    a = int(input())
    A.append(a)

total = sum(A)
for i, a in enumerate(A, 1):
    ans[i] = (total - a) % 2

z = sum(ans[1:K])

for k in range(K + 2, N + 1):
    q = tuple(v for v in range(1, K)) + (k,)
    print("?", *q)
    a = int(input())
    ans[k] = (a - z) % 2

print("!", *ans[1:])
