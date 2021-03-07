N = int(input())
ans = 0
for _ in range(N):
  A, B = map(int, input().split())
  ans += B*(B+1)//2 - A*(A-1)//2
print(ans)