N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [False] * N
for a in A:
  B[a - 1] = True

ans = []
K = []
for i in range(N):
  K.append(i + 1)

  if not B[i]:
    ans.extend(K[::-1])
    K = []

ans.extend(K[::-1])

print(*ans)
