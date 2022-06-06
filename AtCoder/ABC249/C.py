N, K = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
for x in range(1 << N):
  C = [0] * 26
  for i, s in enumerate(S):
    if (1 << i) & x:
      for c in s:
        C[ord(c) - ord('a')] += 1

  ans = max(ans, C.count(K))

print(ans)
