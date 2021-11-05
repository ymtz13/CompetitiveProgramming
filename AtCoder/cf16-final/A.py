from string import ascii_uppercase

H, W = map(int, input().split())
for h in range(1, H + 1):
  S = input().split()
  for s, c in zip(S, ascii_uppercase):
    if s == 'snuke':
      print("{}{}".format(c, h))
