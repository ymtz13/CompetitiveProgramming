N = int(input())
A = list(map(int, input().split()))

S = [0] * (N + 10)
C = [0] * (N + 10)

ans = 0
for i, a in enumerate(A):
    s = S[a]
    c = C[a]

    S[a] += c + i
    C[a] += 1

    ans += (i - 1) * c - s

    # print(i, a, s, c, (i - 1) * c - s)

print(ans)
