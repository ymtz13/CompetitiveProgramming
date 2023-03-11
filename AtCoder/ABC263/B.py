N = int(input())
P = list(map(int, input().split()))
ans = 0
x = N
while x != 1:
  ans += 1
  x = P[x - 2]

print(ans)
