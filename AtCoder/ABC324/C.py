N, T = input().split()
Ss = [input() for _ in range(int(N))]
ans = []


for i, S in enumerate(Ss, 1):
    if len(T) == len(S):
        cnt = 0
        for cT, cS in zip(T, S):
            if cT != cS:
                cnt += 1
        if cnt <= 1:
            ans.append(i)

    if abs(len(T) - len(S)) == 1:
        U = T
        if len(U) > len(S):
            U, S = S, U

        k = len(S) - 1
        for j, (cU, cS) in enumerate(zip(U, S)):
            if cU != cS:
                k = j
                break

        # print(i, k, U[k:], S[k + 1 :])
        if U[k:] == S[k + 1 :]:
            ans.append(i)


print(len(ans))
print(*ans)
