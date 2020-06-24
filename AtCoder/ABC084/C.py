N = int(input())
CSF = [tuple(map(int, input().split())) for _ in range(N-1)]

for st in range(N):
    t = 0
    for i in range(st, N-1):
        C, S, F = CSF[i]
        k = max(0, (t-S + F-1)//F)
        t = S+F*k+C
    print(t)
    
