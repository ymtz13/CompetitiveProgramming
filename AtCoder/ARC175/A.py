mod = 998244353

N = int(input())
P = [p - 1 for p in map(int, input().split())]
S = input()

p0 = P[0]

ans = 0

V = [1] * N
if S[p0] in "L?":
    aL = 1
    V[p0] = 0
    for p in P[1:]:
        s = S[p]
        vR = V[(p + 1) % N]
        V[p] = 0

        if s == "R" and vR:
            aL = 0
            break

        if s == "?" and not vR:
            aL *= 2
            aL %= mod

    ans += aL


V = [1] * N
if S[p0] in "R?":
    aR = 1
    V[p0] = 0
    for p in P[1:]:
        s = S[p]
        vL = V[(p - 1) % N]
        V[p] = 0

        if s == "L" and vL:
            aR = 0
            break

        if s == "?" and not vL:
            aR *= 2
            aR %= mod

    ans += aR

print(ans % mod)
