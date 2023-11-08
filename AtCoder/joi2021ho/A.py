N = int(input())
A = list(map(int, input().split()))
B = A[::-1]

SL = [0]
for a1, a2 in zip(A, A[1:]):
    SL.append(SL[-1] + max(a1 - a2 + 1, 0))

SR = [0]
for a1, a2 in zip(B, B[1:]):
    SR.append(SR[-1] + max(a1 - a2 + 1, 0))

SR.reverse()


ans = 1 << 60
for sl, sr in zip(SL, SR):
    ans = min(ans, max(sl, sr))

print(ans)
