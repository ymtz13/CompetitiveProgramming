N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

ans = 0
for i in range(61):
    n1 = sum([1 for a in A if (a>>i)&1])
    ans += (1<<i)*n1*(N-n1)
    ans %= mod
print(ans)
