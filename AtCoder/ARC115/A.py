N, M = map(int, input().split())
o = e = 0
for _ in range(N):
  if input().count('1') %2:
    o += 1
  else:
    e += 1

print(o * e)
