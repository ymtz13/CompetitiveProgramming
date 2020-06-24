N, L = [int(c) for c in input().split()]
S = L * N + (N-1)*N // 2

if L>0 :
    print(S-L)
elif L+N-1<0:
    print(S-(L+N-1))
else:
    print(S)
