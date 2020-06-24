N, X = [int(c) for c in input().split()]
L = [int(c) for c in input().split()]
n=1
D=0
for l in L:
    D+=l
    if D>X: break
    n+=1

print(n)
