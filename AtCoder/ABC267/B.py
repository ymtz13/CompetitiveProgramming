S = input()
C = [1, 1, 2, 2, 2, 1, 1]

if S[0] == '1':
  print('No')
  exit()

for i, c in enumerate(S):
  if c == '1': continue
  i += 1

  if i in (7, 0): C[0] -= 1
  if i in (4, 0): C[1] -= 1
  if i in (2, 8): C[2] -= 1
  if i in (1, 5): C[3] -= 1
  if i in (3, 9): C[4] -= 1
  if i in (6, 0): C[5] -= 1
  if i in (10, 0): C[6] -= 1

for i in range(7):
  if C[i] == 0: continue
  for j in range(i + 2, 7):
    if C[j] == 0: continue

    if C[i:j].count(0) > 0:
      print('Yes')
      exit()

print('No')
