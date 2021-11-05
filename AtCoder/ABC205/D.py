from bisect import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(Q):
  K = int(input())
  
  ok = 10**19
  ng = 0
  while ok-ng>1:
    tgt = (ok+ng)//2
    
    if tgt - bisect(A, tgt) >= K:
      ok = tgt
    else:
      ng = tgt
  
  print(ok)
