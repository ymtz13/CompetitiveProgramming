def solve(N, S):
    UTPC = "UTPC_"
    n = 0
    iU = iC = None
    for i, c in enumerate(S):
        if c == UTPC[n]:
            n += 1

        if c == "U" and iU is None:
            iU = i
        if c == "C":
            iC = i

    if n < 4:
        return -1

    if "UTPC" in S:
        return 0
    if "UTP" in S:
        return 1
    if "TPC" in S:
        return 1
    if "TP" in S:
        return 2

    iT = None
    for i in range(1, iC):
        c = S[i]
        if S[i - 1] == "U" and c == "T":
            iT = i
            eC = False
        if c == "C":
            eC = True
        if c == "P" and iT is not None:
            if not eC:
                return 2

    iP = None
    for i in range(N - 2, iU, -1):
        c = S[i]
        if S[i + 1] == "C" and c == "P":
            iP = i
            eU = False
        if c == "U":
            eU = True
        if c == "T" and iP is not None:
            if not eU:
                return 2

    iT = None
    for i, c in enumerate(S[iU:iC], iU):
        if c == "T":
            iT = i
            eU = False
            eC = False
        if c == "U":
            eU = True
        if c == "C":
            eC = True
        if c == "P" and iT is not None:
            iP = i

            if not eC or not eU:
                return 3

    return 4


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    S = input()
    a = solve(N, S)
    ans.append(a)

for a in ans:
    print(a)
