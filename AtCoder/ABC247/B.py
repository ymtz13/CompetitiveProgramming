N = int(input())
ST = [tuple(input().split()) for _ in range(N)]

for i, (si, ti) in enumerate(ST):
  ss = tt = False
  for j, (sj, tj) in enumerate(ST):
    if i == j: continue
    if si in (sj, tj): ss = True
    if ti in (sj, tj): tt = True
  if ss and tt:
    print('No')
    exit()

print('Yes')
