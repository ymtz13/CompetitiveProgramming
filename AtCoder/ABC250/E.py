N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

iA = {}
iB = {}
for i, a in enumerate(A):
  if a not in iA: iA[a] = i + 1
for i, b in enumerate(B):
  if b not in iB: iB[b] = i + 1

INF = 1 << 60

sA = [-1]
sB = [-1]
for a in A:
  sA.append(max(sA[-1], iB[a] if a in iB else INF))
for b in B:
  sB.append(max(sB[-1], iA[b] if b in iA else INF))

Q = int(input())
ans = []
for _ in range(Q):
  x, y = map(int, input().split())

  if sA[x] <= y and sB[y] <= x:
    ans.append('Yes')
  else:
    ans.append('No')

for a in ans:
  print(a)
