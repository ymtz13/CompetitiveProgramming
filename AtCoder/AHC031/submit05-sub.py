WIDTH = 1000


def take_max(aaa):
    aamax = [0] * len(aaa[0])
    for aa in aaa:
        aamax = [max(p, a) for p, a in zip(aamax, aa)]
    return aamax


def pack(aa):
    maxrow = sum([(a + WIDTH - 1) // WIDTH for _, a in aa])

    for row in range(maxrow - len(aa) + 1, maxrow + 1):
        cols = [(i, (a + row - 1) // row) for i, a in aa]
        s = sum([a for _, a in cols])

        if s <= WIDTH:
            return (row, cols, maxrow - row)

    return (-1, [], 0)


def split(aa):
    aa = list(enumerate(aa))

    hh0 = [(i, (a + WIDTH - 1) // WIDTH) for i, a in aa]
    sh0 = sum([h for _, h in hh0])
    excess = sh0 - WIDTH

    if excess <= 0:
        return [(h, [(i, WIDTH)]) for i, h in hh0], excess, excess

    aa = sorted(aa, key=lambda ia: ia[1] % WIDTH)

    ret = []
    count = 0
    chunk_size = 5
    excess_improved = excess
    for i in range(0, len(aa), chunk_size):
        chunk = aa[i : i + chunk_size]
        h, cols, improve = pack(chunk)
        if excess_improved > 0 and improve > 0:
            ret.append((h, cols))
            excess_improved -= improve
            count += len(chunk)
        else:
            ret.extend([((a + WIDTH - 1) // WIDTH, [(i, WIDTH)]) for i, a in chunk])

    return ret, excess, excess_improved


def to_coord(num, placement):
    placement = sorted(placement, key=lambda t: t[0])
    ret = [None] * num
    h0 = 0
    hsum = sum([h for h, _ in placement])
    for h, cols in placement:
        h1 = h0 + h
        if h1 == hsum:
            h1 = WIDTH

        wsum = sum([w for _, w in cols])

        w0 = 0
        for i, w in cols:
            w1 = w0 + w
            if w1 == wsum:
                w1 = WIDTH

            ret[i] = (h0, w0, h1, w1)

            w0 = w1
        h0 = h1

    return ret


_, days, num = map(int, input().split())

aaa = [list(map(int, input().split())) for _ in range(days)]

dayl = 0
while dayl < days:
    dayr_max = dayl + 1
    aa = aaa[dayl]
    placement_max, _, _ = split(aa)

    for dayr in range(dayl + 2, days + 1):
        aa = take_max(aaa[dayl:dayr])
        placement, excess, excess_packed = split(aa)
        # print((dayl, dayr, excess, excess_packed))
        if excess_packed > 0:
            break

        dayr_max = dayr
        placement_max = placement

    coord = to_coord(num, placement_max)
    # print(dayl, dayr_max, dayr_max - dayl, len(coord))
    for _ in range(dayl, dayr_max):
        for c in coord:
            pass
            print(*c)

    dayl = dayr_max

exit()

for aa in aaa:
    placement, excess, excess_packed = split(aa)
    coord = to_coord(num, placement)

    for c in coord:
        print(*c)

    # print(excess, excess_packed)
    # assert excess_packed <= 0, (excess, excess_packed)
