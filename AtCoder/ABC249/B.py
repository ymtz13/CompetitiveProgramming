from string import ascii_lowercase, ascii_uppercase

AL = set(ascii_lowercase)
AU = set(ascii_uppercase)

S = input()
SS = set(S)

print('Yes' if len(S) == len(SS) and AL & SS and AU & SS else 'No')
