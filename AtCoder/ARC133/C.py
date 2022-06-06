H, W, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

SA = 0
mA = 0
xA = K - W
for a in A:
  SA += a
  SA %= K
  mA += (xA - a) % K

SB = 0
mB = 0
xB = K - H
for b in B:
  SB += b
  SB %= K
  mB += (xB - b) % K

if SA != SB:
  print(-1)
  exit()

m = max(mA, mB)
print((K - 1) * W * H - m)
