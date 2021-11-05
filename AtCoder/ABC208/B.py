P = int(input())
F = [1]
for i in range(2, 15):
  F.append(F[-1]*i)

ans = 0
for f in F[::-1]:
  ans += P//f
  P %= f

print(ans)
