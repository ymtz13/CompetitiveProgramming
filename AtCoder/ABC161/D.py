K = int(input())

if K<=9:
    print(K)
    exit()

K-=9

def append_ll(array, t, ll):
    global k
    
    array[t].append(ll)
    k += 1
    if k==K:
        print(ll)
        exit()

k = 0
N = 2
lunlun = [None, [None, [1],[2],[3],[4],[5],[6],[7],[8],[9]]]
# lunlun[s][t] := list of s digits lunlun numbers with first number t
while True:
    lunlun_N = [[] for _ in range(10)]

    p = 10**(N-1)
    append_ll(lunlun_N, 1, p)
    
    for d in range(1, N):
        for ll in lunlun[d][1]:
            append_ll(lunlun_N, 1, p+ll)

    for ll in lunlun[N-1][2]:
        append_ll(lunlun_N, 1, p+ll)
    
    for x in range(2, 10):
        for ll in lunlun[N-1][x-1]:
            append_ll(lunlun_N, x, x*p+ll)
            
        for ll in lunlun[N-1][x  ]:
            append_ll(lunlun_N, x, x*p+ll)

        if x==9: continue
        for ll in lunlun[N-1][x+1]:
            append_ll(lunlun_N, x, x*p+ll)

    N+=1
    lunlun.append(lunlun_N)
