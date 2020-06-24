N = int(input())

A=[]
B=[]
for i in range(N):
    a,b = [int(c) for c in input().split()]
    A.append(a)
    B.append(b)
X,Y = sorted(A)[N//2], sorted(B)[N//2]

S=0
for a,b in zip(A,B):
    S += abs(a-X) + abs(b-Y) + b - a

print(S)
