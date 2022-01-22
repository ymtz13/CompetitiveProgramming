from collections import defaultdict

N = int(input())
D = defaultdict(int)
for _ in range(N):
  D[input()] += 1

print(sorted(list(D.items()), key=lambda x: x[1])[-1][0])
