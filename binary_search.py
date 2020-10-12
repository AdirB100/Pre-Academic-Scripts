import math


def bin_search(lst, x):
    lst.sort()
    cnt = 0
    while len(lst) != 0:
        cnt+=1
        if x == lst[math.floor(0.5 * (len(lst) - 1))]:
            return True
        if x > lst[math.floor(0.5 * (len(lst) - 1))]:
            lst = lst[math.floor(0.5 * (len(lst) + 1)):len(lst)]
        else:
            lst = lst[0:math.floor(0.5 * (len(lst) - 1))]
    return cnt





