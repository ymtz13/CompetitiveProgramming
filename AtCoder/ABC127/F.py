from heapq import heappush, heappop

Q = int(input())

hL = []
hR = []
sL = sR = 0

s = 0
for _ in range(Q):
  q = tuple(map(int, input().split()))

  if q[0] == 1:
    _, a, b = q
    s += b

    if hR and a > hR[0]:
      heappush(hR, a)
      sR += a
    else:
      heappush(hL, -a)
      sL += a

    if len(hL) > len(hR) + 1:
      x = -heappop(hL)
      heappush(hR, x)
      sL -= x
      sR += x

    if len(hR) > len(hL):
      x = heappop(hR)
      heappush(hL, -x)
      sR -= x
      sL += x

  if q[0] == 2:
    x = -hL[0]
    f = s + sR - x * len(hR) + x * len(hL) - sL
    print(x, f)
