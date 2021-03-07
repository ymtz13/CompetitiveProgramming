from bisect import bisect

N, M = map(int, input().split())
H = sorted(list(map(int, input().split())))
W = sorted(list(map(int, input().split())))

PF = [0]
for i in range(0, N-1, 2):
  PF.append(PF[-1] + H[i+1]-H[i])

PB = [0]
for i in range(0, N-1, 2):
  PB.append(PB[-1] + H[N-1-i]-H[N-2-i])

ans = 10**20
for w in W:
  i = bisect(H, w)
  nf = i//2
  nb = (N-1)//2 - nf
  s = PF[nf] + PB[nb]
  s += H[i]-w if i%2==0 else w-H[i-1]
  ans = min(ans, s)
print(ans)
