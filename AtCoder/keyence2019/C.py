N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

X = sorted([a-b for a, b in zip(A,B)])
Y = [x for x in X if x<0]
ans = len(Y)
Z = sum(Y)

for x in reversed(X):
    if Z>=0: break
    ans += 1
    Z += x

print(ans if Z>=0 else -1)
