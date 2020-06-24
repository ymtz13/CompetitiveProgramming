N = int(input())

r = []
for i in range(N):
    S, P = input().split()
    P = int(P)
    r.append((i+1,S,P))

r.sort(key=lambda x:x[2], reverse=True)
r.sort(key=lambda x:x[1])
for x in r:
    print(x[0])
