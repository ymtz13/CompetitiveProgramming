N, A, X, Y = map(int, input().split())
ans = N*X - max(0, N-A)*(X-Y)
print(ans)
