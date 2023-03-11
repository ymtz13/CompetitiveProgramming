from collections import deque

N, A, B = map(int, input().split())
S = deque(input())

ans = 1 << 60

sA = 0
for _ in range(N):
  sB = 0
  for i in range(N // 2):
    if S[i] != S[-(i + 1)]: sB += B

  ans = min(ans, sA + sB)

  S.append(S.popleft())
  sA += A

print(ans)
