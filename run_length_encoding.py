def txt2rle(st):
    if st == '':
        return []
    if len(st) == 1:
        return [[st, 1]]
    ls = []
    c = 0
    while len(st) > 1:
        cnt = 1
        i = 0
        while st[i] == st[i + 1]:
            cnt += 1
            i += 1
            if i == len(st) - 1:
                c = 1
                break
        ls.append([st[0], cnt])
        if c == 0:
            st = st[i + 1:]
        else:
            st = ''
    if len(st) == 1:
        ls.append([st[0], 1])
    return ls


def rle2txt(ls):
    if not ls:
        return ''
    st = ''
    for i in ls:
        st += i[0] * i[1]
    return st


def rle_ratio(st):
    print('string: ', '\"', st, '\"\nrle: ', txt2rle(st), '\nRatio: ', len(txt2rle(st)) * 2 / len(st), sep='')