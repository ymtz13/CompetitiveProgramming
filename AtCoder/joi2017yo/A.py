A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

ans = 0

if A < 0:
  ans += -A * C + D
  A = 0

ans += (B - A) * E

print(ans)
