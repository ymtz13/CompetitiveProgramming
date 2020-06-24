N = int(input())
chars = 'AGCT'

dp = {}
for c1 in chars:
    for c2 in chars:
        for c3 in chars:
            dp[c1+c2+c3] = 1
dp['AGC'] = dp['ACG'] = dp['GAC'] = 0

def isValid(s):
    return not (s[1:] == 'AGC' or
                s[1:] == 'ACG' or
                s[1:] == 'GAC' or
                (s[0] == 'A' and s[3] == 'C' and 'G' in s[1:3]) )
        
        

for i in range(N-3):
    dp_new = {k:0 for k in dp}
    for k in dp:
        for c in chars:
            if isValid(k+c):
                dp_new[k[1:]+c] += dp[k]
    dp = dp_new

print(sum([v for k,v in dp.items()]) % 1000000007)
