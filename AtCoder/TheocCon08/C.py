N = int(input())
A = [0] + list(map(int,input().split())) + [0]

S_f = [0]*(N+2)
S_b = [0]*(N+2)
for i in range(1,N+1):
    S_f[i]     = S_f[i-1]   + abs(A[i]-A[i-1])
    S_b[N-i+1] = S_b[N-i+2] + abs(A[N-i+1]-A[N-i+2])

print(S_f)
print(S_b)

for i in range(1,N+1):
    print(S_f[i-1]+S_b[i+1]+abs(A[i-1]-A[i+1]))
