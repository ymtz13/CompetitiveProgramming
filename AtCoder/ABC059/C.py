N = int(input())
A = list(map(int, input().split()))

s = max(A[0], +1)
ans_p = abs(A[0]-s)
for a in A[1:]:
    if s>0: b=min(a, -s-1)
    if s<0: b=max(a, -s+1)
    s += b
    ans_p += abs(a-b)

s = min(A[0], -1)
ans_n = abs(A[0]-s)
for a in A[1:]:
    if s>0: b=min(a, -s-1)
    if s<0: b=max(a, -s+1)
    s += b
    ans_n += abs(a-b)

print(min(ans_p, ans_n))
