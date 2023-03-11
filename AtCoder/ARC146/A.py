N = int(input())
A = sorted(list(map(int, input().split())))
X = [[] for _ in range(10)]
for a in A:
  X[len(str(a))].append(a)

B = []
for x in X[::-1]:
  B.extend(sorted(x, reverse=True))

b1, b2, b3 = list(map(str, B[:3]))

C = [
  b1 + b2 + b3,
  b1 + b3 + b2,
  b2 + b1 + b3,
  b2 + b3 + b1,
  b3 + b1 + b2,
  b3 + b2 + b1,
]

ans = max(map(int, C))
print(ans)
