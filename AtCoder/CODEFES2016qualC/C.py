N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

exact = [False]*N

height = [0]*N
height[0] = T[0]
exact[0] = True

for i in range(1,N):
    height[i] = T[i]
    exact[i] = T[i]>T[i-1]

if (exact[-1] and A[-1]!=height[-1]) or A[-1]>height[-1]:
    print(0)
    exit()
    
height[-1] = A[-1]
exact[-1] = True

for i in range(N-1):
    if A[i]>A[i+1]:
        if (exact[i] and A[i]!=height[i]) or A[i]>height[i]:
            print(0)
            exit()
        height[i]=A[i]
        exact[i]=True
    else:
        if exact[i] and A[i]<height[i]:
            print(0)
            exit()
        else:
            height[i]=min(height[i], A[i])

ans=1
mod=10**9+7
for e,h in zip(exact, height):
    if not e:
        ans=(ans*h)%mod

print(ans)
