N = int(input())

P = []

for x in range(2, 1000000):
    s = str(x)
    if "0" in s:
        continue
    r = s[::-1]
    y = int(r)
    if x > y:
        continue

    p = x * y

    P.append((x * y, x, y))

P.sort()
for p in P[:30]:
    print(p)


for i in range(1, 1000001):
    s = str(i)
    if "0" in s:
        continue
    s1 = s + s[::-1]
    s2 = s[:-1] + s[::-1]
    d1 = int(s1)
    d2 = int(s2)

    if N % d1 == 0:
        pass

    if N % d2 == 0:
        pass


al = []
ar = []
for p, x, y in P[::-1]:
    while N % p == 0:
        N //= p
        al.append(str(x))
        ar.append(str(y))

sN = str(N)

if sN != sN[::-1] or "0" in sN:
    print(-1)
    exit()

al.append(str(N))
al.extend(reversed(ar))

print("*".join(al))
