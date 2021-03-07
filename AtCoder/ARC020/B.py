N, C = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = N
for c1 in range(1,11):
  for c2 in range(1,11):
    if c1==c2: continue

    n = 0
    for i, a in enumerate(A):
      c = c1 if i%2==0 else c2
      if a!=c: n += 1
    
    ans = min(ans, n)

print(ans*C)