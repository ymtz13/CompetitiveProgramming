mod = 998244353


N = int(input())
T = input()

offset = N + 2
N2 = (N * 2) + 5
dp = [0] * N2
dp[0 + offset] = 1

F = [1]
for i in range(1, N2):
    F.append(F[-1] * i % mod)


def comb(N, K):
    return F[N] * pow(F[N - K], mod - 2, mod) * pow(F[K], mod - 2, mod) % mod


print(comb(5, 3))


np = T.count("+")
nm = T.count("-")
nq = T.count("?")
lp = lm = lq = 0
ex = 0

for k, c in enumerate(T, 1):
    dp_next = [0] * N2

    if c == "+":
        np -= 1
    if c == "-":
        nm -= 1
    if c == "?":
        nq -= 1

    if c != "-":
        for i in range(1, N2):
            idx = i - offset
            if idx > nm + nq - np:
                break
            dp_next[i] += dp[i - 1]

            diff = (idx - 1) - (lp - lm)
            # lqPlus + lqMinus = lq
            # lqPlus - lqMinus = diff
            # 2 * lqPlus = lq + diff

            if (lq + diff) % 2:
                continue

            lqPlus = (lq + diff) // 2
            if lqPlus < 0 or lq < lqPlus:
                continue
            print(lq, diff, lqPlus, comb(lq, lqPlus))

            v = comb(lq, lqPlus) * min(abs(idx), abs(idx - 1))
            if v:
                print(k, idx, ":", min(abs(idx), abs(idx - 1)), v)
            ex += v

    if c != "+":
        for i in range(N2 - 2, -1, -1):
            idx = i - offset
            if -idx > np + nq - nm:
                break
            dp_next[i] += dp[i + 1]

            diff = (idx + 1) - (lp - lm)
            # lqPlus + lqMinus = lq
            # lqPlus - lqMinus = diff
            # 2 * lqPlus = lq + diff

            if (lq + diff) % 2:
                continue

            lqPlus = (lq + diff) // 2
            if lqPlus < 0 or lq < lqPlus:
                continue
            print(lq, diff, lqPlus, comb(lq, lqPlus))

            v = comb(lq, lqPlus) * min(abs(idx), abs(idx + 1))
            if v:
                print(k, idx, ":", min(abs(idx), abs(idx + 1)), v)
            ex += v

    if c == "+":
        lp += 1
    if c == "-":
        lm += 1
    if c == "?":
        lq += 1

    dp = dp_next
    print(dp)

base = dp[0 + offset] * N
print(base)
print(ex)

print((base + ex) % mod)
