N = int(input())
A = list(map(int, input().split()))
B = set(A)
C = list(B)

if max(A)==0:
    print('Yes')
    exit()
    
if N%3!=0:
    print('No')
    exit()
    
if (len(B)==3 and
    C[0]^C[1]==C[2] and
    A.count(C[0])==N//3 and
    A.count(C[1])==N//3 and
    A.count(C[2])==N//3):
    print('Yes')
    exit()

if (len(B)==2 and
    min(C)==0 and
    A.count(0)==N//3 and
    A.count(max(C))==2*N//3):
    print('Yes')
    exit()

print('No')
