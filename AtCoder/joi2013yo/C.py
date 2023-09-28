N = int(input())
S = input()

ans = 0
for _ in range(N):
    X = input()

    a = 0
    for st in range(len(X)):
        for p in range(1, 102):
            T = X[st::p]
            if len(T) < len(S):
                break
            if S in T:
                a = 1
                break

        if a == 1:
            break

    ans += a


print(ans)
