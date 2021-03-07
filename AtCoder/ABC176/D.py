H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())

S = ['#'*(W+4)]*(H+4)
for h in range(2, H+2):
    S[h] = '##' + input() + '##'

T = [[-1]*(W+4) for _ in range(H+4)]

f = 0
for h in range(2,H+2):
    for w in range(2,W+2):
        if S[h][w]=='#' or T[h][w]!=-1: continue
        
        queue = [(h,w)]
        iq = 0
        while iq<len(queue):
            ph, pw = queue[iq]
            iq += 1

            if S[ph][pw]=='#' or T[ph][pw]!=-1: continue
            
            T[ph][pw] = f
            queue.append((ph+1,pw  ))
            queue.append((ph-1,pw  ))
            queue.append((ph  ,pw+1))
            queue.append((ph  ,pw-1))

        f += 1

P = [set() for _ in range(f)]
    
for h in range(2,H+2):
    for w in range(2,W+2):
        f = T[h][w]
        if f==-1: continue
        for h2 in range(h-2, h+3):
            for w2 in range(w-2, w+3):
                f2 = T[h2][w2]
                if f2==-1: continue
                if f!=f2: P[f].add(f2)

N = [-1]*len(P)
queue = [(T[Ch+1][Cw+1], 0)]
iq = 0
while iq<len(queue):
    f, n = queue[iq]
    iq += 1

    if N[f]!=-1: continue

    N[f] = n
    for f2 in P[f]: queue.append((f2, n+1))

print(N[T[Dh+1][Dw+1]])
