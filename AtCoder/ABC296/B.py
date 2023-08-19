for row in range(8, 0, -1):
    S = input()
    for col, c in zip("abcdefgh", S):
        if c == "*":
            print("{}{}".format(col, row))
            exit()
