n, k = map(int, input().split())
s = input()

for _ in range(k):
  if len(s)%2==1: s = s + s
  W = []
  for h1, h2 in zip(s[0::2], s[1::2]):
    win = h1
    if h1=='R' and h2=='P': win = h2
    if h1=='P' and h2=='S': win = h2
    if h1=='S' and h2=='R': win = h2
    W.append(win)
  s = ''.join(W)

print(s[0])
