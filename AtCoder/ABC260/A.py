S = input()

for c in S:
  if S.count(c) == 1:
    print(c)
    exit()

print(-1)
