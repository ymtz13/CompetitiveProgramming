N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ta = tb = 0
m = 0
while m<M and tb+B[m]<=K:
    tb += B[m]
    m += 1
ans = m

for n in range(1,N+1):
    ta += A[n-1]
    while ta+tb>K and m>0:
        m -= 1
        tb -= B[m]
    if ta+tb>K:
        break
    ans = max(ans, n+m)

print(ans)
