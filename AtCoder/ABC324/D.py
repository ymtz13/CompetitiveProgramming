N = int(input())
S = list(input())
S.sort()

ans = 0
for n in range(3340000):
    s = list(str(n * n))
    s.sort()

    ls = len(s)
    s = ["0"] * (N - ls) + s

    if s == S:
        ans += 1

print(ans)
