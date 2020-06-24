N = int(input())
D = {}
for _ in range(N):
    A = int(input())
    if A not in D: D[A]=0
    D[A]+=1
print(sum([1 for v in D.values() if v%2==1]))
