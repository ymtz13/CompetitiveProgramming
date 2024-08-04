N, S, T, A, B = map(int, input().split())


def f(x):
    return N * B / x + A * x * (x - 1) / 4


l = 1
r = T
while r - l > 1e-3:
    d = (r - l) / 3
    xl = l + d
    xr = r - d

    fl = f(xl)
    fr = f(xr)

    if fl < fr:
        r = xr
    else:
        l = xl

ans = 1 << 60
if S <= T:
    ans = (T - S) * A

for x in range(int(l) - 100, int(r) + 100):
    if x < 1 or T < x:
        continue
    ans = min(ans, f(x))

print(f"{ans:f}")
