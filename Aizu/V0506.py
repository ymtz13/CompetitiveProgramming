while True:
    n=int(input())
    if n==0: break
    s=input()

    for i in range(n):
        c_prev=s[0]
        n_seq=0
        s_new=''
        for c in s:
            if c==c_prev:
                n_seq+=1
            else:
                s_new+='{}{}'.format(n_seq,c_prev)
                c_prev=c
                n_seq=1
        s_new+='{}{}'.format(n_seq,c_prev)
        #print(s_new)
        s=s_new
    print(s)
