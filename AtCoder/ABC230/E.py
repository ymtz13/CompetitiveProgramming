N = int(input())

if N==1:
  print(1)
  exit()

if N==2:
  print(3)
  exit()


for n in range(1, N + 1):
  if n * n >= N: break

s1 = 0
for i in range(1, N):
  q = N // i
  if q < n: break
  s1 += q

ml = i
s2 = 0
for q in range(n - 1, 0, -1):
  if N // ml < q: continue

  ok = ml
  ng = N + 1
  while ng - ok > 1:
    tgt = (ng + ok) // 2
    if N // tgt < q:
      ng = tgt
    else:
      ok = tgt
  mr = ok
  s2 += (mr - ml + 1) * q

  ml = ok + 1

print(s1 + s2)
