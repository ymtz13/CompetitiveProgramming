n_dataset=1

while True:
    W = int(input())
    if W==0 : break
    N = int(input())
    items = {}
    for i in range(N):
        v, w = [int(v) for v in input().split(',')]
        if w not in items:
            items[w]=[]
        items[w].append(v)

    for k in items:
        items[k].sort(reverse=True)

    #print(items)

    if 0 in items:
        answerlist={ 0:(sum(items[0]),{0:len(items[0])}) }
    else:
        answerlist={0: (0,{}) }

    for w in range(1,W+1):
        newAnswerCandidates=[]
        for w_sub in answerlist: # 0~w-1
            answer_sub=answerlist[w_sub]
            w_new = w-w_sub
            num_all   = len(items[w_new]) if w_new in items else 0
            num_added = answer_sub[1][w_new] if w_new in answer_sub[1] else 0
            if num_all > num_added:
                #print("{:4} {:4} {:4} {:4} {:4}".format(w,w_sub,w_new,num_all,num_added))
                totalVal = answer_sub[0] + items[w_new][num_added]
                numItems = answer_sub[1].copy()
                if w_new not in numItems:
                    numItems[w_new]=0
                numItems[w_new]+=1
                newAnswerCandidates.append((totalVal,numItems))
        if newAnswerCandidates:
            #print(w,newAnswerCandidates)
            answerlist[w]=max(newAnswerCandidates, key=lambda x:x[0])

    #for ll in answerlist:
    #    print("{:4}".format(ll),answerlist[ll])

    w = max(answerlist, key=lambda k:answerlist[k][0])
    print("Case {}:".format(n_dataset))
    print(w)
    print(answerlist[w][0])
    n_dataset+=1
