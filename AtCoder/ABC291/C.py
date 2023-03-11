N = int(input())
S = input()

T = 1000000
x = y = 0
D = set([0])
ans = 'No'

for c in S:
  if c == 'R': x += 1
  if c == 'L': x -= 1
  if c == 'U': y += 1
  if c == 'D': y -= 1

  v = x * T + y
  if v in D:
    ans = 'Yes'
    break

  D.add(v)

print(ans)
