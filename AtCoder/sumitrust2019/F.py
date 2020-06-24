T1, T2 = list(map(int, input().split()))
A1, A2 = list(map(int, input().split()))
B1, B2 = list(map(int, input().split()))

if A1*T1+A2*T2==B1*T1+B2*T2:
    print('infinity')
    exit()

if A1*T1+A2*T2 < B1*T1+B2*T2:
    A1, B1 = B1, A1
    A2, B2 = B2, A2

if A1>B1:
    print(0)
    exit()

Dtot = (A1*T1+A2*T2) - (B1*T1+B2*T2)
Dmin = (B1*T1) - (A1*T1)

ans = 2*((Dmin-1)//Dtot) + 1
if Dmin%Dtot==0: ans+=1
print(ans)
