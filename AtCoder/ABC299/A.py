N = int(input())
S = input()

cnt = 0
ans = "out"
for c in S:
    if c == "|":
        cnt += 1

    if c == "*" and cnt == 1:
        ans = "in"

print(ans)
