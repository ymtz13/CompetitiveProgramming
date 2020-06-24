S = input()
K = int(input())
for i,c in enumerate(S):
    if c!='1': break
print(1 if c=='1' or K<i+1 else c)
