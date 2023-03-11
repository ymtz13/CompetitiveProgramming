N, Q = map(int, input().split())
S = input()

i = 0
ans = []
for _ in range(Q):
  t, x = map(int, input().split())
  if t == 1:
    i -= x
    i %= N
  else:
    ans.append(S[(i + x - 1) % N])

for a in ans:
  print(a)
