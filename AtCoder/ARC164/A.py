T = int(input())

ans = []
for _ in range(T):
    N, K = map(int, input().split())

    n = N
    m = 0
    while n:
        m += n % 3
        n //= 3

    if K % 2 == m % 2 and m <= K and K <= N:
        ans.append("Yes")
    else:
        ans.append("No")

for a in ans:
    print(a)
