N = int(input())
S = input()
T = input()

X = [s != t for s, t in zip(S, T)].count(True)
if X % 2 == 1:
  print(-1)
  exit()

ds = dt = 0
ans = []
for s, t in zip(S, T):
  if s == t:
    ans.append('0')
  else:
    if s == '1':
      if ds - dt < X:
        ans.append('0')
        ds += 1
      else:
        ans.append('1')
        dt += 1

    if t == '1':
      if dt - ds < X:
        ans.append('0')
        dt += 1
      else:
        ans.append('1')
        ds += 1

    X -= 1

print(''.join(ans))
