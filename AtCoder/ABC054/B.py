N, M = list(map(int, input().split()))
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

for oh in range(N-M+1):
    for ow in range(N-M+1):
        match = True
        for ih in range(M):
            for iw in range(M):
                if A[oh+ih][ow+iw]!=B[ih][iw]:
                    match = False
                    break
            if not match: break
        if match:
            print('Yes')
            exit()
print('No')
