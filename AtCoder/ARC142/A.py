N, K = input().split()
N = int(N)

if K[-1] == '0':
  print(0)
  exit()

rK = int(K[::-1])
K = int(K)

if rK < K:
  print(0)
  exit()

S = set()
for i in range(15):
  S.add(rK * (10**i))
  S.add(K * (10**i))

S = {s for s in S if s <= N}
print(len(S))
