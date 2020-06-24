N, W = list(map(int, input().split()))

w1, v = list(map(int, input().split()))
V = [[] for _ in range(4)]
V[0].append(v)

for _ in range(N-1):
    w, v = list(map(int, input().split()))
    V[w-w1].append(v)

S = []
for vl in V:
    vl.sort(reverse=True)
    s = [0]
    for v in vl:
        s.append(s[-1]+v)
    S.append(s)
    
print(V)
print(S)

ans = 0
for n0, s0 in enumerate(S[0]):
    for n1, s1 in enumerate(S[1]):
        for n2, s2 in enumerate(S[2]):
            for n3, s3 in enumerate(S[3]):
                if n0*w1 + n1*(w1+1) + n2*(w1+2) + n3*(w1+3)<=W:
                    ans = max(ans, s0+s1+s2+s3)
print(ans)
