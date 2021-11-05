N = int(input())
A = list(map(int, input().split()))

s = 0
p = None
ans = 0
for a in A + [None]:
  if a!=p:
    ans += s//2
    p = a
    s = 0  
  s += 1
    
print(ans)
