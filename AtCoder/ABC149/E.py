N, M = list(map(int, input().split()))
A = sorted(list(map(int, input().split())), reverse=True)

def check(X):
    i = N-1
    n = 0
    for ax in A:
        while i>=0 and A[i]+ax<X: i-=1
        n+=i+1
    return n>=M

# check(X) := 幸福度がX以上上がる握手をすべて行うとき、握手の回数がM以上になるか？
# check(X)==True となる最大のXを二分探索で求める
min_ng = 10**6
max_ok = 0
while min_ng-max_ok>1:
    tgt = (min_ng+max_ok)//2
    if check(tgt):
        max_ok = tgt
    else:
        min_ng = tgt

i = N-1

k = sum(A)
ans = 0
n = 0
for ax in A:
    while i>=0 and A[i]+ax<max_ok:
        k-=A[i]
        i-=1
    ans += k + ax*(i+1)
    n += i+1
print(ans-max_ok*(n-M))
