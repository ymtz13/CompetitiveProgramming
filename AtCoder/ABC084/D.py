primes = [2]
for c in range(3,10**5+1):
    isPrime = True
    for p in primes:
        if p*p>c: break
        if c%p==0:
            isPrime=False
            break
    if isPrime: primes.append(c)

primeset = set(primes)

like2017s = set([p for p in primes if (p+1)//2 in primeset])

k = [0]*(10**5+10)
for x in range(1, 10**5+10):
    if x in like2017s:
        k[x]=k[x-1]+1
    else:
        k[x]=k[x-1]

Q = int(input())
for _ in range(Q):
    l, r = list(map(int, input().split()))
    print(k[r]-k[l-1])
