chars = [
    "',.!?",
    "abcABC",
    "defDEF",
    "ghiGHI",
    "jklJKL",
    "mnoMNO",
    "pqrsPQRS",
    "tuvTUV",
    "wxyzWXYZ",
]


while True:
    try:
        keys = [int(c) for c in input()] + [-1]
        s=''

        k_prev = -1
        seq = 0
        for k in keys:
            if k != k_prev:
                if k_prev>=1: s+=chars[k_prev-1][seq % len(chars[k_prev-1])]
                seq=0
            else:
                seq+=1
                if k==0 and seq>=1: s+=' '
            k_prev=k

        print(s)
                

    except EOFError:
        break
