N = int(input())
A = list(map(int, input().split()))
R = [0] * 200
for a in A:
  R[a%200] += 1

ans = 0
for r in R:
  ans += r*(r-1)//2

print(ans)
