N = int(input())
A = list(map(int, input().split()))
B = [-1]*100001
b = -1

ans = 0
for i, a in enumerate(A):
  b = max(b, B[a])
  ans = max(ans, i - b)
  B[a] = i
ans = max(ans, N-b-1)

print(ans)
