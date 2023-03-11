N, M, X, T, D = map(int, input().split())

I = T - X * D
print(min(I + M * D, T))
