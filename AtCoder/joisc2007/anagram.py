from string import ascii_uppercase

S = input()

F = [1]
for i in range(1, 21):
    F.append(F[-1] * i)


def h(S):
    cnt = [0] * 26
    for c in S:
        cnt[ord(c) - ord("A")] += 1

    r = F[len(S)]
    for n in cnt:
        r //= F[n]

    return r


def solve(S):
    if len(S) == 1:
        return 0

    x = 0
    for c in set(S[1:]):
        if c >= S[0]:
            continue

        i = S.find(c)
        T = S[:i] + S[i + 1 :]

        x += h(T)

    return x + solve(S[1:])


print(solve(S) + 1)
