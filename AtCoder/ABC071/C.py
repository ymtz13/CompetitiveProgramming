import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
D = {}
for a in A:
    if a not in D: D[a] = 0
    D[a] += 1

E =  sorted([(k,v) for k,v in D.items() if v>=2] + [(0,4)])

l1, n1 = E[-1]
if n1>=4:
    print(l1*l1)
else:
    l2, n2 = E[-2]
    print(l1*l2)
    
