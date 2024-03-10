N = int(input())
A = list(map(int, input().split()))

P = [[None] * 11 for _ in range(N)]
L = [None] * 11

ans = 0

m = -1
for i, a in enumerate(A):
    for d in range(-4, 5):
        b = a + d
        if b < 1 or 10 < b:
            continue

        j = L[b]
        if j is None:
            continue

        P[i][b] = j

        c = b + d
        if c < 1 or 10 < c:
            continue

        k = P[j][c]
        # print("i,j,k,a,b,c", i, j, k, a, b, c)
        if k is not None:
            m = max(m, k)

    L[a] = i

    # print(i, m)

    ans += m + 1

print(ans)
