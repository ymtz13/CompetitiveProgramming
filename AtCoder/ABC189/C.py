N = int(input())
A = list(map(int, input().split()))

ans = 0
for l, al in enumerate(A):
  m = al
  for n, ar in enumerate(A[l:]):
    m = min(m, ar)
    ans = max(ans, (n+1)*m)

print(ans)
