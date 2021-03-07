S = input()
T = input()
L = len(T)
ans = L
for i in range(len(S)-L+1):
    s = S[i:i+L]
    cnt = 0
    for cs, ct in zip(s, T):
        if cs!=ct: cnt+=1
    ans = min(ans, cnt)
print(ans)
