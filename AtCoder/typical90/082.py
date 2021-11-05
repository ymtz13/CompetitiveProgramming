mod = 10**9+7

def count(X):
  if X==0: return 0
  ret = 0
  for d in range(20):
    #if X<10**d:
    #  ret += X
    #  break
    ret += max(X*(X+1)//2 - (10**d-1)*(10**d)//2, 0)
    ret %= mod
    #print(ret)

  return ret

L, R = map(int, input().split())
ans = (count(R) - count(L-1)) % mod
print(ans)
