N = int(input())
A = list(map(int, input().split()))
X = sum(A)/10
A += A
S = set([0])
s = 0
for a in A:
  s += a
  S.add(s)
  if s-X in S:
    print('Yes')
    exit()

print('No')
