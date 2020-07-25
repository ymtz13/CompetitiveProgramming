import heapq as hq

T = int(input())
for _ in range(T):
    N = int(input())
    Cp = []
    Cn = []
    ans = 0
    for _ in range(N):
        K, L, R = map(int, input().split())
        D = L-R
        if D>=0:
            ans += R
            Cp.append((K,D))
        else:
            ans += L
            Cn.append((N-K,-D))

    Cp = sorted(Cp, reverse=True)
    Cn = sorted(Cn, reverse=True)
    Np = len(Cp)
    Nn = len(Cn)

    i = 0
    h = []
    for n in range(Np, 0, -1):
        while i<Np:
            k, d = Cp[i]
            if k<n: break
            hq.heappush(h, -d)
            i+=1

        if len(h): ans += -hq.heappop(h)

    i = 0
    h = []
    for n in range(Nn, 0, -1):
        while i<Nn:
            k, d = Cn[i]
            if k<n: break
            hq.heappush(h, -d)
            i+=1

        if len(h): ans += -hq.heappop(h)

    print(ans)
