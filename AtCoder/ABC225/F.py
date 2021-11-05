N, K = map(int, input().split())
S = sorted([input() for _ in range(N)])

ans = []
for i in range(K):
  s0 = S[0]
  SS = [s for s in S if s[:len(s0)] == s0]

  for i, s in S:
    if s[:len(s0)] != s0: continue
    

