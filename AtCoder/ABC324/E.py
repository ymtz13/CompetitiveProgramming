N, T = input().split()
N = int(N)
Ss = [input() for _ in range(N)]

lT = len(T)
U = T[::-1]
T += "."
U += "."


F = []
B = []

for S in Ss:
    i = 0
    for c in S:
        if c == T[i]:
            i += 1
    F.append(i)

    i = 0
    for c in reversed(S):
        if c == U[i]:
            i += 1
    B.append(i)


F.sort()
B.sort(reverse=True)
B.append(-N - 10)

ans = 0
i = 0
for f in F:
    while f + B[i] >= lT:
        i += 1
    ans += i

print(ans)
