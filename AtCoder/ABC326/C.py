N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

A.append(1 << 60)

i = 0
ans = 0
for j, a in enumerate(A[:-1]):
    while a + M > A[i]:
        i += 1
    ans = max(ans, i - j)

print(ans)
