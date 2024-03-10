N = int(input())
S = [1 if c == "A" else -1 for c in input()]

if S[0] == -1:
    S = [-c for c in S]

S = S[1:]

V = [0]
for c in S:
    V.append(V[-1] + c)

ans = 1
for c, v in zip(S[::-1], V[::-1]):
    if c == 1:
        continue

    if v in (-2, -1, 0):
        ans += 1

print(ans)
