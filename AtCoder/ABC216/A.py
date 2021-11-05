X, Y = map(int, input().split('.'))
S = '-' if Y <= 2 else '+' if Y >= 7 else ''
print(str(X) + S)
