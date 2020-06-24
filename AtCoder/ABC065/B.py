N = int(input())
A = [int(input()) for _ in range(N)]

i = 1
ans = 0
while i!=2 and i>0:
    i_next = A[i-1]
    A[i-1] = -A[i-1]
    i = i_next
    ans += 1
print(ans if i>0 else -1)
