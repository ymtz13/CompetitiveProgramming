A = int(input())
B = int(input())

ans = A * (10**9) + (B//2) * 10
if B % 2 == 1:
  ans += 5

print(ans)
