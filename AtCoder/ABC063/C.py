N = int(input())
S = [int(input()) for _ in range(N)]
t = sum(S)

if t%10==0:
    f = True
    for s in sorted(S):
        if s%10!=0:
            f = False
            break
    if f:
        print(0)
    else:
        print(t-s)
else:
    print(t)
