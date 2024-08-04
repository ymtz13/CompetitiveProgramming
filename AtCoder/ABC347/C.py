N, A, B = map(int, input().split())
D = list(map(int, input().split()))

X = [d % (A + B) for d in D]
X.sort()
X = X + [X[0] + (A + B)]


for p, a in zip(X, X[1:]):
    if a - p > B:
        print("Yes")
        exit()

print("No")
