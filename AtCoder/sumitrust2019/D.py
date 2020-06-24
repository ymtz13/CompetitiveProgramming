N = int(input())
S = input()

s1 = set()
s2 = set()
s3 = set()
for c in S:
    for c2 in s2: s3.add(c2+c)
    for c1 in s1: s2.add(c1+c)
    s1.add(c)

print(len(s3))
        
