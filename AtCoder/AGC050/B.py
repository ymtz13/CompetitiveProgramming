N = int(input())
A = [int(input()) for _ in range(N)]
S = sum([a for a in A if a > 0])

ans = 0
for i in range(N - 2):
  s1 = S + sum([a for a in A[i:i + 3] if a < 0])
  s2 = S - sum([a for a in A[i:i + 3] if a > 0])
  ans = max(ans, s1, s2)

print(ans)
