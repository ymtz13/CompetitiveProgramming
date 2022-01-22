N = int(input())
A = sorted([tuple(map(int, input().split())) for _ in range(N)])

ans = 1
for i in range(1, N):
  if A[i] != A[i - 1]: ans += 1
print(ans)
