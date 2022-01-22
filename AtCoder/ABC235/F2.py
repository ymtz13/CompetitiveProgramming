mod = 998244353

dpC = [[0] * 1024]
dpS = [[0] * 1024]
dpC[0][0] = 1
dpS[0][0] = 0

B = [1<<i for i in range(10)]

d = 1
for _ in range(10**4):
  dpC_now = dpC[-1]
  dpS_now = dpS[-1]

  dpC_next = [0] * 1024
  dpS_next = [0] * 1024

  for i, y in enumerate(B):
    for x in range(1024):
      z = x | y
      cnt = dpC_now[x]
      dpC_next[z] += cnt
      dpS_next[z] += dpS_now[x] + cnt * d * i

      dpC_next[z] %= mod
      dpS_next[z] %= mod

  dpC.append(dpC_next)
  dpS.append(dpS_next)

  print(_)

  d *= 10
  d %= mod

print(dpC[3][0b111])

# 012 021 102 120 201 210
# 001 010 100 011 110 101



N = list(map(int, input()))
M = int(input())
C = list(map(int, input().split()))

c = sum([B[i] for i in C])

for k in range(1, len(N)):
  for i, b in enumerate(B):
    
