N, K = map(int, input().split())
A = list(map(int, input().split()))
Sp = [0]
Sn = [0]
for a in A:
  Sp.append(Sp[-1] + max(0, a))
  Sn.append(Sn[-1] + min(0, a))

ans = 0
for i in range(N - K + 1):
  ap = Sp[-1] + Sn[i + K] - Sn[i]
  an = Sp[-1] - Sp[i + K] + Sp[i]

  ans = max(ans, ap, an)

print(ans)
