A, X, M = map(int, input().split())

P = 1
S = 0
ans = 0
for i in range(50):
    b = 1 << i
    if X & b:
        ans += P * pow(A, S, M)
        ans %= M
        S += b

    P += pow(A, b, M) * P
    P %= M

print(ans)
