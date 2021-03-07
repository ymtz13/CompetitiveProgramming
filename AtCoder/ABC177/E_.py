N = 1000000
isPrime = [0]*(N+1)
primes = []
for x in range(2, N+1):
    p = 2
    prime = True
    while p*p<=x:
        if x%p==0:
            prime=False
            break
        p+=1
    if prime: isPrime[x]=1
    if prime: primes.append(x)

print(','.join(map(str,primes)))
