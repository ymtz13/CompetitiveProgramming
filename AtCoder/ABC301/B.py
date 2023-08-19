N = int(input())
A = list(map(int, input().split()))

ans = []

for f, t in zip(A, A[1:]):
    d = 1 if f < t else -1
    ans.extend(range(f, t, d))

ans.append(A[-1])

print(*ans)
