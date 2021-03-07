N = int(input())
S = input()

D = []
C = []
M = [None]*N
m = 0
for i, c in enumerate(S):
    if c=='M': m+=1
    M[i] = m
    
    if c=='D': D.append(i)
    if c=='C': C.append(i)

Q = int(input())
K = map(int, input().split())



for k in K:

    i = 0
    for c in C:
        while D[i+1]<c-k: i+=1
        
