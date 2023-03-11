N, K = map(int, input().split())
S = input()

ans = []
k = 0
for c in S:
  if c == 'o' and k < K:
    a = 'o'
    k += 1
  else:
    a = 'x'
  ans.append(a)

print(''.join(ans))
