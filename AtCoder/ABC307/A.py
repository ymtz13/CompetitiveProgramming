N = int(input())
A = list(map(int, input().split()))
ans = [sum(A[i * 7 : i * 7 + 7]) for i in range(N)]
print(*ans)
