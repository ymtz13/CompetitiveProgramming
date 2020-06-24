N = int(input())
A = [(i+1, int(a)) for i,a in enumerate(input().split())]
l = [i for i,a in sorted(A, key=lambda x: x[1])]
print(*l)
    
