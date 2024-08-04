N, Q = map(int, input().split())
X = list(map(int, input().split()))

a = 0
A = []
P = [None] * (N + 1)
S = set()
ans = [0] * (N + 1)

for i, x in enumerate(X):
    a += len(S)
    A.append(a)

    if x in S:
        S.remove(x)
        p = P[x]
        diff = a - A[p]
        ans[x] += diff
    else:
        S.add(x)
        P[x] = i

a += len(S)
A.append(a)
for x in S:
    p = P[x]
    diff = a - A[p]
    ans[x] += diff

# print(A)
print(*ans[1:])
