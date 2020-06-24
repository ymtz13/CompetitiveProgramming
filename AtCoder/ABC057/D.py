def comb(n, k):
    x = y = 1
    for i in range(k):
        x *= n-i
        y *= i+1
    return x//y

N, A, B = list(map(int, input().split()))
V = sorted(list(map(int, input().split())), reverse=True)

if V[0]==V[A-1]:
    n = 0
    for v in V:
        if v!=V[0]: break
        n += 1

    ans = 0
    for k in range(A, min(B,n)+1):
        ans += comb(n, k)

else:
    n = k = 0
    for i,v in enumerate(V):
        if v==V[A-1]:
            if i<A: k += 1
            n += 1
    ans = comb(n,k)

print(sum(V[:A])/A)
print(ans)
