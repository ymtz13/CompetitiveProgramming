N = 10**6
D = [None]*(N+1) # D[x] != the largest prime factor of x.
for p in range(2,N+1):
    if D[p] is not None: continue
    for x in range(p, N+1, p): D[x] = p

def isPrime(x):
    return D[x]==x

def factorize(x):
    f = {}
    while x>1:
        d = D[x]
        x //= D[x]
        if d not in f: f[d] = 0
        f[d] += 1
    return f

def divisors(x):
    f = list(factorize(x).items())
    divisors = []
    
    def dfs(i, d):
        if i==len(f):
            divisors.append(d)
            return
        
        p, n = f[i]
        q = 1
        for x in range(n+1):
            dfs(i+1, d*q)
            q *= p
    
    dfs(0, 1)
    return divisors
    

for x in range(1,20):
    print(x, D[x], factorize(x), divisors(x))
