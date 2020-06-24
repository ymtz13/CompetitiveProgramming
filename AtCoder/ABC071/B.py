print((sorted(list({chr(i) for i in range(ord('a'),ord('z')+1)}-set(input())))+['None'])[0])
