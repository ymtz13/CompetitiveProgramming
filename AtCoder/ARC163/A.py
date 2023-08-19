T = int(input())

Ans = []
for _ in range(T):
    N = int(input())
    S = input()
    X = [ord(c) for c in S]

    c0 = X[0]

    if max(X) > c0:
        Ans.append("Yes")
        continue

    if N == 2:
        Ans.append("No")
        continue

    if (S[0] * 2) in S:
        Ans.append("Yes")
        continue

    f = False
    for n in range(1, N):
        s1 = S[:n]
        s2 = S[n:]
        if s1 < s2:
            Ans.append("Yes")
            f = True
            break
    if f:
        continue

    Ans.append("No")


for ans in Ans:
    print(ans)
