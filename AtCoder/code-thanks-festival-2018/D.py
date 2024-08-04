S = input()
d = "z"

ans = 0
for c in S:
    if c <= d:
        d = c
        ans += 1

print(ans)
