R, G, B, N = [int(c) for c in input().split()]

n=0
for r in range(N//R+1):
    N2 = N-R*r
    if N2==0:
        n+=1
        continue
    
    for g in range(N2//G+1):
        if (N2-G*g)%B==0:
            n+=1

print(n)
    
