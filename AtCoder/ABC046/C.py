N = int(input())
t = a = 1
for _ in range(N):
    T, A = list(map(int, input().split()))
    # t->cT,  a->cA
    # min(c) s.t. cT>=t && cA>=a
    c = max((t+T-1)//T, (a+A-1)//A)
    t, a = c*T, c*A
print(t+a)
