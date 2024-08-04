def solve(K):
    k = K
    for n in range(1, 20):
        c = pow(9, n)  # ちょうどn桁のNeq Numberの数
        if k <= c:
            break
        k -= c

    # ちょうどn桁のNeq Numberのうちk番目
    k -= 1
    D = []
    for _ in range(n):
        D.append(k % 9)
        k //= 9
    D.reverse()

    ret = []
    prev = 0
    for d in D:
        X = [x for x in range(10) if x != prev]
        x = X[d]
        ret.append(x)
        prev = x

    # print(K, n, k, D, ret)
    return "".join(map(str, ret))


T = int(input())
ans = []
for _ in range(T):
    K = int(input())
    ans.append(solve(K))


for a in ans:
    print(a)
