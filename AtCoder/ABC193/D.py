K = int(input())
S_ = input()
T_ = input()
S = [S_.count(str(i)) for i in range(10)]
T = [T_.count(str(i)) for i in range(10)]
R = [0] + [K]*9
for i in range(10):
  R[i] -= S[i] + T[i]

def point(X, x):
  X[x] += 1
  p = 0
  for i in range(10):
    p += i * 10**X[i]
  X[x] -= 1
  return p

sumR = sum(R)
total = sumR * (sumR - 1)

ans = 0
chk = 0

for s in range(1, 10):
  for t in range(1, 10):
    pS = point(S, s)
    pT = point(T, t)

    if s==t:
      r = R[s]
      prob = r*(r-1)
      if pS>pT: ans += prob
      chk += prob
    
    else:
      rs = R[s]
      rt = R[t]
      prob = rs*rt
      if pS>pT: ans += prob
      chk += prob

print(ans/total)
