N = int(input())
A = [int(input()) for _ in range(N)]

max_l, max_r = [A[0]], [A[-1]]
for i in range(N-1):
    max_l.append(max(A[i+1],   max_l[i]))
    max_r.append(max(A[N-2-i], max_r[i]))

print(max_r[-2])
for i in range(1,N-1):
    print(max(max_r[-2-i], max_l[i-1]))
print(max_l[N-2])
