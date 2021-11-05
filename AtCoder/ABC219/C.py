X = input()
T = [None] * 26
orda = ord('a')
for i, x in enumerate(X):
  T[ord(x) - orda] = i

N = int(input())
K = []
for _ in range(N):
  S = input()
  k = tuple(T[ord(c) - orda] for c in S)
  K.append((k, S))

for _, S in sorted(K):
  print(S)
