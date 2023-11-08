from heapq import heappop, heappush, heapify

N, D, K = map(int, input().split())
PS = [tuple(map(int, input().split())) for _ in range(N)]

N2 = N * 2 + 5
E = N + 1

heap0 = [-(s + 1) * N2 + E * 2 + p - 1 for p, s in PS]
heapify(heap0)


def f(X):
    heap = heap0[:]
    cnt = [0, 0]

    while heap:
        q = heappop(heap)

        time = -(q // N2)
        cp = q % N2
        c = cp // 2
        p = cp % 2

        if time < 0:
            return False

        print(f"time={time}, c={c}, p={p}")
        # print(time, c if c < E else "E", p)

        if c == E:
            cnt[p] += 1

            event_remain = X - cnt[p]
            time_move = D + K * event_remain
            time_departure = time - 1 - time_move

            heappush(heap, -time_departure * N2 + cnt[p] * 2 + 1 - p)
        else:
            cnt[p] = max(cnt[p], c)

        if cnt[p] >= X:
            return True

    return False


f(12)
exit()

ng = N + 1
ok = 1
while ng - ok > 1:
    tgt = (ok + ng) // 2
    if f(tgt):
        ok = tgt
    else:
        ng = tgt

print(ok)
