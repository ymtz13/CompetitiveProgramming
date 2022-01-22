N, K = map(int, input().split())
s = 0
ans = None
for n in range(1, N + 1):
  a = int(input())
  s += a
  if s >= K: ans = ans or n

print(ans)
