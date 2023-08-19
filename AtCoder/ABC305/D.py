from bisect import bisect

N = int(input())
A = list(map(int, input().split()))

A0 = A[0::2]
A1 = A[1::2]

S = [0]
for a0, a1 in zip(A0[1:], A1):
    S.append(S[-1] + a0 - a1)


def f(t):
    i0 = bisect(A0, t) - 1
    i1 = bisect(A1, t) - 1

    r = S[i0]
    if i1 >= i0:
        r += t - A1[i1]

    return r


Q = int(input())
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    ans.append(f(r) - f(l))


for a in ans:
    print(a)
