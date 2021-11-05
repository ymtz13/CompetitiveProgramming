from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
ans = 0

X = [[] for _ in range(32)]
for a in A:
  for i in range(32):
    b = 1 << i
    if a & b:
      X[i].append(a)
      break

for i, x in enumerate(X):
  D = defaultdict(int)
  for a in sorted(x):
    a >>= (i + 1)
    D[a] += 1

  for a, d in D.items():
    print(a)

    for j in range(32):
      c = 1 << j
      if c > a: break
    k = c - 1 - a

    print('{:010b}'.format(a))
    print('{:010b}'.format(k))
    print()
    ans += min(D[a], D[k])

print(ans)
