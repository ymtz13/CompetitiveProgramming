N = int(input())
S = [input() for _ in range(N)]

Mrow = [0] * N
Mcol = [0] * N

for i, s in enumerate(S):
    for j, c in enumerate(s):
        if c == "o":
            Mrow[i] += 1
            Mcol[j] += 1

ans = 0
for i, s in enumerate(S):
    for j, c in enumerate(s):
        if c == "o":
            v = (Mrow[i] - 1) * (Mcol[j] - 1)
            ans += v

print(ans)
