N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = [a // K for a in A if a % K == 0]
print(*ans)
