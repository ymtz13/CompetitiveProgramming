primes = [2]
for p in range(3,55556,2):
    isPrime = True
    for q in primes:
        if q*q>p:break
        if p%q==0:
            isPrime = False
            break
    if isPrime: primes.append(p)

primes_1 = [p for p in primes if p%5==1]
print(*(primes_1[:int(input())]))
