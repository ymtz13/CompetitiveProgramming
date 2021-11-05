N = int(input())
A = list(map(int ,input().split()))

p = A[0]
d = '='
ans = 1
for a in A[1:]:
  if a < p:
    if d == '+':
      ans += 1
      d = '='
    else:
      d = '-'

  if a > p:
    if d == '-':
      ans += 1
      d = '='
    else:
      d = '+'

  #print(a, d, ans)
  p = a

print(ans)
