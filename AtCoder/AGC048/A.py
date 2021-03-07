T = int(input())
a = ord('a')
P = [ord(c) for c in 'atcoder_']

for _ in range(T):
    S = [ord(c) for c in input()]
    L = len(S)
    if S>P:
        print(0)
        continue

    #N = [[] for _ in range(26)]
    #for i,c in enumerate(S): N[ord(c)-a].append(i)

    ans = 10**10
    U = [0]*26
    cost = 0
    for i,c in enumerate(S):
        # S[i] > "atcoder"[i]
        for j in range(i, L):
            if S[j]>P[i]:
                ans = min(ans, cost + j-i)
                break
            
        if i>7: break

        # S[i] = "atcoder"
        ok = False
        for j in range(i, L):
            if S[j]==P[i]:
                R = S[i:j]
                S[i] = S[j]
                S[i+1:j+1] = R
                cost += j-i
                ok = True
                break
            
        if not ok: break

    print(ans if ans < 10**10 else -1)

        
            
