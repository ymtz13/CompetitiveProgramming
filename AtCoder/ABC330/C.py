D = int(input())

S = [x * x for x in range(2_000_000)]

i = 0
ans = 1 << 60
for x2 in reversed(S):
    while True:
        cur = abs(x2 + S[i] - D)
        nxt = abs(x2 + S[i + 1] - D)
        if cur <= nxt:
            break
        i += 1

    ans = min(ans, cur)

print(ans)
