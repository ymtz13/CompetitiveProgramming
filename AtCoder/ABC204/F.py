import numpy as np

H, W = map(int, input().split())

M = np.zeros((1<<H, 1<<H), int)

for p1 in range(1<<H):
  for p2 in range(1<<H):
    v = 1
    streak = [[]]
    for h in range(H):
      b = 1<<h
      if (p1&b) and (p2&b): v = 0
      if not (p1&b) and not (p2&b):
        streak[-1].append(h)
      else:
        streak.append([])

    for s in streak:
      if len(s)==2: v*= 2
      if len(s)==3: v*= 3
      if len(s)==4: v*= 5
      if len(s)==5: v*= 8
      if len(s)==6: v*= 13
    M[p2, p1] = v

print(M)
v = np.zeros((1<<H, ), int)
v[0] = 1
#W = W-1
mod = 998244353
for i in range(200):
  if W&(1<<i): v = np.dot(M, v) % mod
  M = np.dot(M, M) % mod

print(v % mod)
