from bisect import bisect

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

ok = 1 << 60
ng = 0
while ok - ng > 1:
    tgt = (ok + ng) // 2

    a = bisect(A, tgt)
    b = M - bisect(B, tgt - 1)

    if a >= b:
        ok = tgt
    else:
        ng = tgt


print(ok)
