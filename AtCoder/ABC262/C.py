N = int(input())
A = [-1] + list(map(int, input().split()))
ans = cnt = 0

for i, a in enumerate(A[1:], 1):
  if i==a:
    ans += cnt
    cnt += 1
  else:
    if i < a and A[a] == i:
      ans += 1

print(ans)
