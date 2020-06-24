S = input()
X = [None]*200001 + list(S) + [None]*200001
ifront = 200000
iback = 200001 + len(S)
rev = False

Q = int(input())
for _ in range(Q):
    query = input().split()
    if len(query)==1: rev = not rev
    else:
        F = int(query[1])
        C = query[2]

        if (not rev and F==1) or (rev and F==2):
            X[ifront] = C
            ifront -= 1
        else:
            X[iback] = C
            iback += 1

ans = ''.join(X[ifront+1:iback])
print(ans if not rev else ans[::-1])
