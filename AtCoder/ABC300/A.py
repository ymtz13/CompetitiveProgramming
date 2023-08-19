N, A, B = map(int, input().split())
C = list(map(int, input().split()))

for i, c in enumerate(C, 1):
    if A + B == c:
        print(i)
