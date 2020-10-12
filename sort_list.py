def sort_list(lst):
    lst2 = []
    min_i = 0
    while len(lst) != 0:
        for i in range(len(lst)):
            if lst[min_i] > lst[i]:
                min_i = i
        lst2.append(lst[min_i])
        lst.pop(min_i)
        min_i = 0
    return lst2