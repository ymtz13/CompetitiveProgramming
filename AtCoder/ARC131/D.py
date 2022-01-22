from heapq import heappush, heappop
from bisect import bisect

N, M, D = map(int, input().split())
RR = list(map(int, input().split()))
SS = list(map(int, input().split()))

R = []
S = [0]
for r, s in zip(RR[::-1], SS[::-1]):
  R.append(-r)
  S.append(s)
for r, s in zip(RR[1:], SS[1:] + [0]):
  R.append(r + 1)
  S.append(s)
R.append(1 << 60)

#print(R)
#print(S)


def get(x):
  i = bisect(R, x)
  return i, S[i], R[i]

x0 = -(N // 2 + 1) * D
heap = []

score = 0
for n in range(N):
  x = x0 + n * D
  i, s, r = get(x)
  score += s
  heappush(heap, (r - x, i, x))

ans = score
#print(score, x0, heap)

while True:
  d, _, _ = heap[0]
  if d > D * 3: break

  while heap[0][0] == d:
    d, i, x = heappop(heap)
    score += S[i + 1] - S[i]
    #print(i, d, x, S[i + 1], S[i], score)
    heappush(heap, (R[i + 1] - x, i + 1, x))

  #print('upDate', d, score)
  ans = max(ans, score)

print(ans)
