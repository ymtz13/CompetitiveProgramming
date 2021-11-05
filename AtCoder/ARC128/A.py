N = int(input())
A = list(map(int, input().split()))

S = [[]]
p = 1 << 60
for a in A:
  if a > p: S.append([])
  S[-1].append(a)
  p = a

print(S)

ans = []
for s in S:
  a = [0] * len(s)
  if len(s) >= 2:
    a[0] = a[-1] = 1
  ans.extend(a)

print(' '.join(map(str, ans)))
