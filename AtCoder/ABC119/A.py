S = input()
y, m, d = int(S[:4]), int(S[5:7]), int(S[8:])
print('Heisei' if y<2019 or (y==2019 and (m<4 or (m==4 and d<=30))) else 'TBD')
