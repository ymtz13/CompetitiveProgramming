N = int(input())
A, B, C = map(int, input().split())

ans = 10000
for a in range(10000):
  for b in range(10000):
    r = N - A*a + B*b
    if r>=0 and r%C==0: ans = min(ans, a+b+r//C)

print(ans)
