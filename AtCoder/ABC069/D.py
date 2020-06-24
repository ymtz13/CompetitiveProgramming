import sys
input = sys.stdin.readline

H, W = list(map(int, input().split()))
N = int(input())
A = list(map(int, input().split()))

na = 0
ia = 0
for h in range(H):
    l = []
    for w in range(W):
        if na==0:
            na = A[ia]
            ia += 1
        l.append(ia)
        na -= 1
    if h%2==1: l = l[::-1]
    print(*l)
