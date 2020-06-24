N = int(input())
X = {c:0 for c in 'MARCH'}
for _ in range(N):
    c = input()[0]
    if c in X: X[c]+=1

ans = 0
for i1 in range(5):
    for i2 in range(i1+1,5):
        for i3 in range(i2+1,5):
            ans += X['MARCH'[i1]]*X['MARCH'[i2]]*X['MARCH'[i3]]
print(ans)
