N = int(input())

ans = 0
for A in range(1, 10000):
  if A * A * A > N: break

  for B in range(A, 1000000):
    if A * B * B > N: break
    Cmax = N // (A * B)
    ans += Cmax - B + 1

print(ans)
