N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def f(T):
    C = B[:]

    i = 0
    for _ in range(K):
        t = T - A[i]
        while t > 0:
            c = min(t, C[i])
            C[i] -= c
            t -= c
            if C[i] == 0:
                if i == N - 1:
                    break
                t -= A[i + 1] - A[i]
                i += 1

    return C[-1] == 0


ok = sum(B) + max(A) + 10
ng = 0

while ok - ng > 1:
    tgt = (ok + ng) // 2

    if f(tgt):
        ok = tgt
    else:
        ng = tgt

print(ok)
