K = int(input())
ans = 0
for A in range(1, K+1):
  L = K // A
  for B in range(1, L+1):
    ans += L // B
print(ans)