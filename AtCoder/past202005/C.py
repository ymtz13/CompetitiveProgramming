A, R, N = map(int, input().split())
ans = A
M = N-1
while M and ans<=1000000000:
    if M&1: ans*=R
    R*=R
    M>>=1

print(ans if ans<=1000000000 else 'large')
