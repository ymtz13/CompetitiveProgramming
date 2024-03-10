N, M = map(int, input().split())
S = input()
T = input()


def No():
    print("No")
    exit()


if S[0] != T[0]:
    No()

I = [0]
for j, (p, c) in enumerate(zip(S, S[1:]), 1):
    K = []
    for k, t in enumerate(T):
        if c == t and j >= k and N - j >= M - k:
            K.append(k)

    # print(j, c, K)

    Inext = []
    for k in K:
        if k == 0 or M - 1 in I or k - 1 in I:
            Inext.append(k)

    I = Inext

    if not I:
        No()


print("Yes")
