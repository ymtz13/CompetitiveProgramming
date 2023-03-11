S = input()
T = input()

F = [True]
for s, t in zip(S, T):
  m = s == '?' or t == '?' or s == t
  F.append(F[-1] and m)

B = [True]
for s, t in zip(S[::-1], T[::-1]):
  m = s == '?' or t == '?' or s == t
  B.append(B[-1] and m)

lenT = len(T)
for x in range(lenT + 1):
  m = F[x] and B[lenT - x]
  print('Yes' if m else 'No')
