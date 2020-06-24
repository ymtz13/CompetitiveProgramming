while True:
    n,k=[int(e) for e in input().split()]
    if(n==0):
        break
    arr=[0]*k
    s=0
    m=0
    for i in range(n):
        #print(i,m,arr)
        s+=int(input())
        old=arr[i%k]
        arr[i%k]=s
        if(i==k-1):
            m=s
        if(i>=k):
            m=max(s-old,m)

    print(m)
