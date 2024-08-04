N = 5
A = [3, 2, 1, 2, 3]


def solve(A):
    S = set()
    D = set()
    for b in range(1, 1 << len(A)):
        s = []
        for i, a in enumerate(A):
            if (b >> i) & 1:
                s.append(a)
        s = tuple(s)
        if s in S:
            D.add(s)
        else:
            S.add(s)

    print(len(S), len(D), len(S) - len(D), S.difference(D))
    return S


solve([1, 2, 3, 4])
solve([2, 1, 1, 2])
solve([1, 2, 1, 2])
