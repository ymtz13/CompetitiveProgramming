N = int(input())
S = input()
T = [None] * N
n = 0
ans = N
for c in S:
  if c=='x' and n>=2 and T[n-2]=='f' and T[n-1]=='o':
    ans -= 3
    n -= 2
  else:
    T[n] = c
    n += 1
print(ans)