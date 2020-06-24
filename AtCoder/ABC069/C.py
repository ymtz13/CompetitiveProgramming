import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

n0,n2,n4 = 0,0,0
for a in A:
    if a%4==0: n4+=1
    elif a%2==0: n2+=1
    else: n0+=1

if n2==0:
    print('Yes' if n0<=n4+1 else 'No')
else:
    print('Yes' if n0<=n4   else 'No')
