S = input()
N = len(S)
ans = 0
for sep in range(2**(N-1)):
    p = 0
    for i in range(N):
        if (sep>>i)&1 or i==N-1:
            ans += int(S[p:i+1])
            p = i+1

print(ans)
