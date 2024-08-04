N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

if K >= 1:
    print("Yes")
    print(*A)
else:
    if sum(A) < K:
        print("No")
    else:
        print("Yes")
        print(*reversed(A))
