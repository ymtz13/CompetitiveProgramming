S = input()
print('Yes' if len(S)%2 == 0 and set(S[0::2]) == {'h'} and set(S[1::2]) == {'i'} else 'No')