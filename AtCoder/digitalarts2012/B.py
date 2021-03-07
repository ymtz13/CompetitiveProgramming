C = [ord(c)-ord('a')+1 for c in input()]
N = sum(C)

if N==1 or N==26*20:
    print('NO')
    exit()

ans = []
for i in range(20):
    if N==0: break
    d = min(N, 26)
    if i==0 and d==C[0]: d -= 1
    N -= d
    ans.append(chr(d+ord('a')-1))

print(''.join(ans))
    
