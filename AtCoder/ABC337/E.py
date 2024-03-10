N = int(input())
X = [[] for _ in range(10)]

for n in range(N):
    for i in range(10):
        b = 1 << i
        if n & b:
            X[i].append(n + 1)

X = [x for x in X if x]


print(len(X))
for x in X:
    print(len(x), *x)

S = input()

ans = 1
r = 1
for c in S:
    ans += int(c) * r
    r <<= 1

print(ans)
