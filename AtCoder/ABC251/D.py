input()

X1 = list(range(1, 100))
X2 = [x * 100 for x in X1]
X3 = [x * 100 for x in X2]
ans = X1 + X2 + X3

print(len(ans))
print(' '.join(map(str, ans)))

