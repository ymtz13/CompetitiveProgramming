I = []
for i in range(10):
  S = input()
  if not '#' in S: continue

  I.append(i + 1)
  J = [j + 1 for j, c in enumerate(S) if c == '#']

A = min(I)
B = max(I)
C = min(J)
D = max(J)

print(A, B)
print(C, D)
