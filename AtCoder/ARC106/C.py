N, M = map(int, input().split())

if N==1 and M==0:
    print(1,2)
    exit()

if M<0 or N-1<=M:
    print(-1)
    exit()

K = 10**6
print(1, K)
for i in range(M+1):
    print(i*2+2, i*2+3)

for i in range(N-2-M):
    print(K+i*2+2, K+i*2+3)

