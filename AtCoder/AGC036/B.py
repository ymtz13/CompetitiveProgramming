N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

M = [None]*(max(A)+1)
T = [None]*N
for i,a in enumerate(A):
    M[a] = i

for i,a in enumerate(A):
    T[M[a]]=(i+1)%N
    M[a]=i

ptr=0
ptr_head = [ptr]
while True:
    ptr_next = T[ptr]
    if ptr_next==0: break
    if ptr_next <= ptr+1: ptr_head.append(ptr_next)
    ptr = ptr_next

period = len(ptr_head)
if T[-1]==0: period+=1

if K % period==0:
    print()
    exit()

ret = []
ptr = ptr_head[K % period - 1]
while ptr<N:
    ptr_next = T[ptr]
    if ptr_next > ptr+1:
        ptr = ptr_next
    elif ptr_next==0 and ptr!=N-1:
        break
    else:
        ret.append(A[ptr])
        ptr+=1

print(' '.join(map(str, ret)))
