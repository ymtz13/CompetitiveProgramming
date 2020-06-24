while True:
    try:
        s=input()
        nJOI = nIOI = 0
        for i in range(len(s)-2):
            nJOI += s[i:i+3]=='JOI'
            nIOI += s[i:i+3]=='IOI'
        print(nJOI)
        print(nIOI)
            
    except EOFError:
        break
