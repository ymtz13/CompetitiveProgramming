N = int(input())
H = [0]+list(map(int, input().split()))
C = [10**10] + [0]*N
for i in range(2,N+1):
    C[i] = min(C[i-1]+abs(H[i-1]-H[i]), C[i-2]+abs(H[i-2]-H[i]))
print(C[-1])
