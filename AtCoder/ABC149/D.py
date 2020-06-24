N, K = list(map(int, input().split()))
R, S, P = list(map(int, input().split()))
T = input()
X = {'r':P, 's':R, 'p':S}
win = [False]*K

ans = 0
for i in range(N):
    if i<K or T[i]!=T[i-K] or not win[i%K]:
        ans += X[T[i]]
        win[i%K]=True
    else:
        win[i%K]=False

print(ans)
