N = input()
K = len(N) - 1
ans = (K//3)*(int(N)+1)

for i in range(3, K+1, 3):
  ans -= 10**i

print(ans)

