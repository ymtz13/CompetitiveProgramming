N = int(input())
A = list(map(int, input().split()))
im, m = 0, 0
for i,a in enumerate(A):
    if abs(a)>abs(m):
        m = a
        im = i

operations = []
for i in range(N):
    if i==im: continue
    operations.append((im+1, i+1))
    A[i] += A[im]

if m>=0:
    for i in range(N-1):
        operations.append((i+1, i+2))
        A[i+1] += A[i]

else:
    for i in range(N-1, 0, -1):
        operations.append((i+1, i))
        A[i-1] += A[i]

print(A)
print(len(operations))
for x, y in operations:
    print(x,y)
