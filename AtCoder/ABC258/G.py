N = int(input())

A = [tuple(map(int, input())) for _ in range(N)]

# n3     + n2     + n1     + n0     = N*(N-1)*(N-2)/6
# n3 * 3 + n2                       = p1
#                   n1     + n0 * 3 = p0
# n3 * 3 + n2 * 2 + n1              = M

