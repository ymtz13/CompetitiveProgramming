N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [a-b for a,b in zip(A,B)]

Ce = sorted([c for c in C[0::2]], reverse=True)
Co = sorted([c for c in C[1::2]], reverse=True)

score = sum(B)
ans = score
for p in range(N//2):
    score += Ce[p] + Co[p]
    ans = max(ans, score)

print(ans)
