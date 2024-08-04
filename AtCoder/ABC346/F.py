orda = ord("a")


def solve(N, S, T):
    S = [ord(c) - orda for c in S]
    T = [ord(c) - orda for c in T]

    pos = [[] for _ in range(26)]
    cnt = [[0] for _ in range(26)]
    for i, c in enumerate(S):
        pos[c].append(i)

        for ccnt in cnt:
            ccnt.append(ccnt[-1])

        cnt[c][-1] += 1

    def f(k):
        n = i = 0
        for t in T:
            c = len(pos[t])
            if c == 0:
                return False

            cL = cnt[t][i]
            cR = c - cL

            if k <= cR:
                inxt = pos[t][cL + k - 1] + 1
            else:
                kk = k - cR  # > 0
                nnxt = n + 1 + (kk - 1) // c
                inxt = pos[t][(kk - 1) % c] + 1
                n = nnxt

            i = inxt

        return n < N or n == N and i == 0

    ok = 0
    ng = len(S) * N // len(T) + 1
    while ng - ok > 1:
        tgt = (ng + ok) // 2
        if f(tgt):
            ok = tgt
        else:
            ng = tgt

    return ok


N = int(input())
S = input()
T = input()

print(solve(N, S, T))
