digits = [str(c) for c in range(10)]

while True:
    try:
        lhs, rhs = input().split('=')
        t1, t2 = lhs.split('+')
        
        out = 'NA'
        for d in digits:
            if d=='0' and ((t1[0]=='X' and len(t1)>1) or
                           (t2[0]=='X' and len(t2)>1) or
                           (rhs[0]=='X' and len(rhs)>1)) : continue
            if int(t1.replace('X', d)) + int(t2.replace('X', d)) == int(rhs.replace('X', d)):
                out = d
                break
        print(out)

    except EOFError:
        break
