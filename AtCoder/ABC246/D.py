N = int(input())

Q = 0
for Q in range(N):
  if Q * Q * Q > N: break


def f(a):
  ng = -1
  ok = Q + 1

  while ok - ng > 1:
    tgt = (ok + ng) // 2
    if (a + tgt) * (a * a + tgt * tgt) >= N:
      ok = tgt
    else:
      ng = tgt

  return (a + ok) * (a * a + ok * ok)


ans = N * N * N

for a in range(Q + 1):
  ans = min(ans, f(a))

print(ans)
