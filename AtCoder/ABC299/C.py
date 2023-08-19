N = int(input())
S = input()

if "-" not in S or "o" not in S:
    print(-1)
    exit()

X = S.split("-")
ans = max([len(x) for x in X])
print(ans)
