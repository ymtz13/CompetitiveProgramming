N = int(input())
if N==0:
    print(0)
    exit()

sign = 1
S = []
while N!=0:
    S.append(N%2)
    N = (N - S[-1]*sign)//2
    sign *= -1
    print(N, S)

print(''.join(map(str, reversed(S))))
