N = int(input())
S = input()
unpaired_open, unpaired_close = 0, 0
for c in S:
    if c=='(': unpaired_open+=1
    elif unpaired_open==0: unpaired_close += 1
    else: unpaired_open -=1

print('('*unpaired_close + S + ')'*unpaired_open)
    
    
