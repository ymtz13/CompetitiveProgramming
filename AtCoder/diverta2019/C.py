N = int(input())
n=0
a_tail = b_head = both = 0
for _ in range(N):
    s = input()
    n += s.count('AB')

    if s[-1]=='A' and s[0]=='B':
        both += 1
    elif s[-1]=='A':
        a_tail += 1
    elif s[0]=='B':
        b_head += 1

if a_tail==0 and b_head==0:
    if both==0:
        print(n)
    else:
        print(n+both-1)
else:
    print(n+min(a_tail,b_head)+both)
