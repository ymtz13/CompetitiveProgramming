S = input()
N = int(input())

M = 60

S = "0" * (M - len(S)) + S

B = []
for i in range(60):
    B.append((N >> i) & 1)
B = B[::-1]

print(S)
print(B)


INF = 1 << 120


def dfs(i, f=True):
    if i == 60:
        return 0

    s = S[i]
    b = B[i]

    if s == "?":
        pass

    else:
        s = int(s)
        if f and s == 1 and b == 0:
            return -INF
        if s == 0 and b == 1:
            f = False
        return dfs(i + 1, f) + (1 << (59 - i)) * s


print(dfs(S, B, 0))
