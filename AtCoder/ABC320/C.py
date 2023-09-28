M = int(input())
S1 = input()
S2 = input()
S3 = input()

S1 *= 3
S2 *= 3
S3 *= 3

ans = INF = 10000

for i1, c1 in enumerate(S1):
  for i2, c2 in enumerate(S2):
    if c1 != c2:
      continue
    if i1 == i2:
      continue
    for i3, c3 in enumerate(S3):
      if c1 != c3:
        continue
      if i1 == i3 or i2 == i3:
        continue
      ans = min(ans, max(i1, i2, i3))

print(ans if ans < INF else -1)
