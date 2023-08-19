mod = 998244353


def sqrt(N):
    for i in range(2, N + 5):
        if i * i > N:
            return i - 1


T = int(input())

Ans = []
for _ in range(T):
    N = int(input())
    sqrtN = sqrt(N)
    ans = pow(sqrtN, 3, mod)

    x_prev = sqrtN
    for y in range(sqrtN, 0, -1):
        x = N // y
        x_cnt = x - x_prev
        x_prev = x

        ans += x_cnt * y * y * 3
        ans %= mod

    Ans.append(ans)

for a in Ans:
    print(a)
