N = int(input())

M = 0
while M*M<=N: M += 1

ans = 1
P = [True]* (M+1)
for p in range(2, M+1):
  if P[p]:
    for q in range(p+p, M+1, p):
      P[q] = False
    
    if N%p==0: ans = p
    while N%p==0: N//=p
      

print(max(ans, N))
