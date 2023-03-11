X, Y, N = map(int, input().split())
Y = min(Y, X * 3)
print(Y * (N // 3) + X * (N % 3))
