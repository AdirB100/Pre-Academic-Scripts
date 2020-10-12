def repeat(st, n):
    st_new = ''
    for i in st:
        st_new += n * i
    print(st_new)
    return st_new


def restore(st, n):
    ls = []
    st_origin = ''
    for i in range(len(st) // n):
        ls.append(st[i * n:(i + 1) * n])
    for i in ls:
        if i.count('1') > i.count('0'):
            st_origin += '1'
        else:
            st_origin += '0'
    print(st_origin)
    return st_origin
