N = int(input())
X = [tuple(map(int, input().split())) for _ in range(N)]
ans = [0] * N

for i in range(3):
    C = [0] * 101
    for x in X:
        C[x[i]] += 1

    for j, x in enumerate(X):
        if C[x[i]] == 1:
            ans[j] += x[i]

for a in ans:
    print(a)
