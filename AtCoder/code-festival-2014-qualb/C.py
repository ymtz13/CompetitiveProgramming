SS = [input() for _ in range(3)]
CC = [[0] * 26 for _ in range(3)]
N = len(SS[0]) // 2

oA = ord('A')
for S, C in zip(SS, CC):
  for c in S:
    C[ord(c) - oA] += 1

n1 = n2 = 0
for c1, c2, c3 in zip(*CC):
  if c1 + c2 < c3:
    print('NO')
    exit()
  n1 += max(0, c3 - c2)
  n2 += max(0, c3 - c1)

if n1 > N or n2 > N:
  print('NO')
  exit()

print('YES')
