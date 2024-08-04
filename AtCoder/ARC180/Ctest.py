def solve(A):
    N = len(A)
    S = set()
    for b in range(1 << N):
        B = A[:]
        s = 0
        for i, a in enumerate(A):
            if (b >> i) & 1:
                s += a
                B[i] = s
        S.add(tuple(B))

    return S


# print(solve([1, 1, 2]))
# print(solve([1, -1, 1, -1]))

s = solve([2, -2, 1, 3, -3, -1, -2, -3])
print(len(s))

s = solve([2, -2, 1, 3, -3, -1, -2, -3, 0, 0])
print(len(s))

# {
#     (1, -1, 2, 1),  1
#     (1, 0, 1, -1), 0
#     (1, -1, 1, -1), [0]
#     (1, -1, 1, -2), -2
#     (1, 0, 1, 0), 0
#     (1, -1, 0, -1), 0
#     (1, -1, 2, -1),2
#     (1, -1, 1, 0)0
# }
