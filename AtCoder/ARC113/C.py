from collections import defaultdict

S = input()[::-1]
p = '_'
D = defaultdict(int)
ans = 0
for i, s in enumerate(S):
  if s==p:
    ans += i - D[s]
    D = defaultdict(int)
    D[s] = i + 1
  
  else:
    p = s
    D[s] += 1

print(ans)
