N = int(input())
A = list(map(int, input().split()))

M = 1 << 18

C = [0] * M
for a in A:
  C[a] += 1

ans = 0

for a, ca in enumerate(C[1:], 1):
  for p in range(a, M, a):
    b = p // a
    ans += ca * C[b] * C[p]

print(ans)
