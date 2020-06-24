s = input()
K = int(input())
d = set()

for l in range(1, K+1):
    for i in range(len(s)+1-l):
        d |= {s[i:i+l]}

print(sorted(list(d))[K-1])
