def solve(P, A):
    A0 = A[0]
    C = [a - A0 for a in A[1:]]

    B = [A0]

    for n in range(1, P):
        s = 0
        for m, c in enumerate(C, 1):
            s += c * pow(m, n * (P - 2), P)
            s %= P

        B.append(s * (P - 1) % P)

    return B


P = int(input())
A = list(map(int, input().split()))

ans = solve(P, A)
print(*ans)


# f(0)   = b[0]                                                        = a[  0]
# f(1)   = b[0] +     1 b[1] +     1^2 b[2] + ... +     1^(p-1) b[p-1] = a[  1]
# f(2)   = b[0] +     2 b[1] +     2^2 b[2] + ... +     2^(p-1) b[p-1] = a[  2]
# ...
# f(p-1) = b[0] + (p-1) b[1] + (p-1)^2 b[2] + ... + (p-1)^(p-1) b[p-1] = a[p-1]

# [[ 1,   1,       1, ...,           1]  [[b[  1]]  =
#  [ 1,   2,     2^2, ...,     2^(p-1)]   [b[  2]]
#  [                  ...,            ]   [ ...  ]
#  [ 1, p-1, (p-1)^2, ..., (p-1)^(p-1)]]  [b[p-1]]]
