N = int(input())
S = []
for i in range(1, N + 1):
  S = S + [i] + S

print(' '.join(map(str, S)))
