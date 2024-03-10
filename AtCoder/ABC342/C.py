N = int(input())
S = input()
Q = int(input())
Queries = [input().split() for _ in range(Q)]

oa = ord("a")
M = list(range(26))

for c, d in Queries:
    c = ord(c) - oa
    d = ord(d) - oa
    for i in range(26):
        if M[i] == c:
            M[i] = d

ans = []
for s in S:
    s = ord(s) - oa
    ans.append(chr(M[s] + oa))

print("".join(ans))
