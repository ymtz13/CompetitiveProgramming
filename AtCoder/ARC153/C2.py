N = int(input())
A = list(map(int, input().split()))
flip = A[-1] == +1

A = [-a for a in A]

ok = False
c = d = 0
for i in range(N - 1, -1, -1):
  d += c
  c += A[i]
  if c > 0:
    ok = True
    break

if not ok:
  print('No')
  exit()

X = i

ans = []
s = 0
for i, a in enumerate(A[:X]):
  ans.append(i)
  s += i * a

x = max(X, -s, d)
ans.append(x)
s += x

for i, a in enumerate(A[X + 1:-1]):
  v = x + i + 1
  ans.append(v)
  s += v * a

ans.append(s)

print('Yes')
print(*ans)
