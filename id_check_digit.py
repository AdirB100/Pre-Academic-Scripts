def id_check_digit():
    idn = list(input('First 8 digits of ID Number: '))
    for i in range(1, len(idn), 2):
        idn[i] = str(int(idn[i]) * 2)
    a = ''
    for j in idn:
        a += j
    summ = 0
    for k in a:
        summ += int(k)
    l = 10
    while l < summ:
        l += 10
    print('**************\nCheck digit: ' + str(l - summ) + '\n**************')
    return l - summ


id_check_digit()
