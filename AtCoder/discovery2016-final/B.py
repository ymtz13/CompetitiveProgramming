import heapq

N, X = map(int, input().split())
T = map(int, input().split())
A = map(int, input().split())
D = sorted(list(zip(T, A)), reverse=True)

def check(T):
    h = []
    i = 0
    x = 0
    for t in range(T, 0, -1):
        while i<N and D[i][0]>=t:
            heapq.heappush(h, -D[i][1])
            i+=1
        if len(h): x += -heapq.heappop(h)
    return x>=X

max_ng = 0
min_ok = time_ng = D[0][0]+1
while min_ok-max_ng>1:
    tgt = (min_ok+max_ng)//2
    ok = check(tgt)
    if ok:
        min_ok = tgt
    else:
        max_ng = tgt

print(min_ok if min_ok<time_ng else -1)
