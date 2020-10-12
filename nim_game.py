import random


def dec2bin(n):
    if n == 0:
        return 0
    elif n < 0 or type(n) == float:
        print('ERROR')
        return None
    s = ''
    while n:
        s = str(n % 2) + s
        n //= 2
    return int(s)


def unbalanced(n1, n2):
    a = n1
    b = n2
    n1 = dec2bin(n1)
    n2 = dec2bin(n2)
    m = max([len(str(n1)), len(str(n2))])
    lst = []
    cnt = 0
    for i in range(1, m + 1):
        if n1 % 10 != 0:
            cnt += 1
        if n2 % 10 != 0:
            cnt += 1
        lst.append(cnt)
        cnt = 0
        n1 = n1 // 10
        n2 = n2 // 10
    lst.reverse()
    # lst  contains the times of the number of factors of two that consist the given inputs, from largest to smallest
    cnt = 0
    lst2 = []
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            cnt += 1
            lst2.append(len(lst) - i - 1)
    if cnt == 0:
        return []
    # lst2 is a list which contains the powers of 2 which are not balanced
    return lst2


def nimbalance(n1, n2, n3):
    a = n1
    b = n2
    c = n3
    n1 = dec2bin(n1)
    n2 = dec2bin(n2)
    n3 = dec2bin(n3)
    m = max([len(str(n1)), len(str(n2)), len(str(n3))])
    lst = []
    cnt = 0
    for i in range(1, m + 1):
        if n1 % 10 != 0:
            cnt += 1
        if n2 % 10 != 0:
            cnt += 1
        if n3 % 10 != 0:
            cnt += 1
        lst.append(cnt)
        cnt = 0
        n1 = n1 // 10
        n2 = n2 // 10
        n3 = n3 // 10
    lst.reverse()
    # lst contains the count of the number of factors of two that consist the given inputs, from largest to smallest
    cnt = 0
    lst2 = []
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            cnt += 1
            lst2.append(len(lst) - i - 1)
    if cnt == 0:
        return 'Already balanced!'
    # lst2 is a list which contains the powers of 2 which are not balanced from left to right
    # print('lst2 =',lst2)
    if a == b == c:
        lstarg = [a, b, c]
        rand = random.choice(['a', 'b', 'c'])
        if rand == 'a':
            lstarg[0] = 0
        elif rand == 'b':
            lstarg[1] = 0
        else:
            lstarg[2] = 0
        return tuple(lstarg)
    maxpower = max(lst2)
    # print('maxpower =',maxpower)
    cnt = 0
    lst3 = []
    for i in [a, b, c]:
        j = i
        q = list(str(dec2bin(i)))
        # print('q =',q)
        if len(q) >= maxpower + 1:
            if q[len(q) - 1 - maxpower] == '1':
                lst3.append(j)
                cnt += 1
    # lst3 is a list which holds the values of the arguments which have the largest unbalanced power of two
    # print('cnt =',cnt) #for test only
    # print('lst3 =',lst3) #for test only

    if cnt == 1:
        shm = 0
        if a == lst3[0]:
            for i in unbalanced(b, c):
                shm += 2 ** i
            a = shm
        elif b == lst3[0]:
            for i in unbalanced(a, c):
                shm += 2 ** i
            b = shm
        else:
            for i in unbalanced(a, b):
                shm += 2 ** i
            c = shm
        return (a, b, c)

    elif cnt == 3:
        while cnt != 1 and len(lst2) > 0:
            lst3 = []
            cnt = 0
            # print('lst2 before remove =',lst2)
            maxx = max(lst2)
            # print('maxx =',maxx)
            lst2.remove(maxx)
            # print('lst2 after remove =',lst2)
            if len(lst2) != 0:
                maxpower = max(lst2)
                # print('maxpower =',maxpower)
                for i in [a, b, c]:
                    v = list(str(dec2bin(i)))
                    if v[len(v) - 1 - maxpower] == '1':
                        lst3.append(i)
                        cnt += 1
                # print('lst3 =',lst3)
                # print('cnt =',cnt)
                shm = 0
                if a == lst3[0]:
                    # print('unbalanced b,c:',unbalanced(b,c))
                    for i in unbalanced(b, c):
                        shm += 2 ** i
                    a = shm
                elif b == lst3[0]:
                    # print('unbalanced a,c:',unbalanced(a,c))
                    for i in unbalanced(a, c):
                        shm += 2 ** i
                    b = shm
                else:
                    # print('unbalanced a,b:',unbalanced(a,b))
                    for i in unbalanced(a, b):
                        shm += 2 ** i
                    c = shm
                return (a, b, c)
            else:
                lstarg = [a, b, c]
                rand = random.choice(['a', 'b', 'c'])
                if rand == 'a':
                    lstarg[0] = a - 2 ** maxpower
                elif rand == 'b':
                    lstarg[1] = b - 2 ** maxpower
                else:
                    lstarg[2] = c - 2 ** maxpower
                return tuple(lstarg)


def nimguide(a, b, c):
    inputt = [a, b, c]
    if type(nimbalance(a, b, c)) == str:
        print('Already balanced!')
    else:
        outputt = list(nimbalance(a, b, c))
        if outputt[0] != inputt[0]:
            print('Take', inputt[0] - outputt[0], 'from the first spot')
        elif outputt[1] != inputt[1]:
            print('Take', inputt[1] - outputt[1], 'from the scond spot')
        else:
            print('Take', inputt[2] - outputt[2], 'from the third spot')


def nim_game(a, b, c):
    inputt = (a, b, c)
    state = list(inputt)
    print('input: ', inputt)
    q = ''
    while q != '1' and q != '0':
        q = input('Who is first: Smart (enter 1) or Dumb (enter 0)? ')
    if q == '1':
        comp = nimbalance(a, b, c)
        if type(comp) == str:
            spot = random.choice(['a', 'b', 'c'])
            if spot == 'a':
                if state[0] != 0:
                    state[0] -= random.choice(range(1, state[0] + 1))
                    comp = tuple(state)
                    print('Smart move: ', comp)
                else:
                    spot = 'b'
            if spot == 'b':
                if state[1] != 0:
                    state[1] -= random.choice(range(1, state[1] + 1))
                    comp = tuple(state)
                    print('Smart move: ', comp)
                else:
                    spot = 'c'
            if spot == 'c':
                if state[2] != 0:
                    state[2] -= random.choice(range(1, state[2] + 1))
                    comp = tuple(state)
                    print('Smart move: ', comp)
                else:
                    spot = 'a'
                if spot == 'a':
                    if state[0] != 0:
                        state[0] -= random.choice(range(1, state[0] + 1))
                        comp = tuple(state)
                        print('Smart move: ', comp)
        else:
            print('Smart move: ', comp)
        state = list(comp)
        last = '1'
    elif q == '0':
        spot = random.choice(['a', 'b', 'c'])
        if spot == 'a':
            if state[0] != 0:
                state[0] -= random.choice(range(1, state[0] + 1))
                dumb = tuple(state)
                print('Dumb move: ', dumb)
            else:
                spot = 'b'
        if spot == 'b':
            if state[1] != 0:
                state[1] -= random.choice(range(1, state[1] + 1))
                dumb = tuple(state)
                print('Dumb move: ', dumb)
            else:
                spot = 'c'
        if spot == 'c':
            if state[2] != 0:
                state[2] -= random.choice(range(1, state[2] + 1))
                dumb = tuple(state)
                print('Dumb move: ', dumb)
            else:
                spot = 'a'
            if spot == 'a':
                if state[0] != 0:
                    state[0] -= random.choice(range(1, state[0] + 1))
                    dumb = tuple(state)
                    print('Dumb move: ', dumb)
        state = list(dumb)
        last = '0'
    while state != [0, 0, 0]:
        if last == '1':
            spot = random.choice(['a', 'b', 'c'])
            if spot == 'a':
                if state[0] != 0:
                    state[0] -= random.choice(range(1, state[0] + 1))
                    dumb = tuple(state)
                    print('Dumb move: ', dumb)
                else:
                    spot = 'b'
            if spot == 'b':
                if state[1] != 0:
                    state[1] -= random.choice(range(1, state[1] + 1))
                    dumb = tuple(state)
                    print('Dumb move: ', dumb)
                else:
                    spot = 'c'
            if spot == 'c':
                if state[2] != 0:
                    state[2] -= random.choice(range(1, state[2] + 1))
                    dumb = tuple(state)
                    print('Dumb move: ', dumb)
                else:
                    spot = 'a'
                if spot == 'a':
                    if state[0] != 0:
                        state[0] -= random.choice(range(1, state[0] + 1))
                        dumb = tuple(state)
                        print('Dumb move: ', dumb)
            state = list(dumb)
            last = '0'
        elif last == '0':
            comp = nimbalance(state[0], state[1], state[2])
            if type(comp) == str:
                spot = random.choice(['a', 'b', 'c'])
                if spot == 'a':
                    if state[0] != 0:
                        state[0] -= random.choice(range(1, state[0] + 1))
                        comp = tuple(state)
                        print('Smart move: ', comp)
                    else:
                        spot = 'b'
                if spot == 'b':
                    if state[1] != 0:
                        state[1] -= random.choice(range(1, state[1] + 1))
                        comp = tuple(state)
                        print('Smart move: ', comp)
                    else:
                        spot = 'c'
                if spot == 'c':
                    if state[2] != 0:
                        state[2] -= random.choice(range(1, state[2] + 1))
                        comp = tuple(state)
                        print('Smart move: ', comp)
                    else:
                        spot = 'a'
                    if spot == 'a':
                        if state[0] != 0:
                            state[0] -= random.choice(range(1, state[0] + 1))
                            comp = tuple(state)
                            print('Smart move: ', comp)
            else:
                print('Smart move: ', comp)
            state = list(comp)
            last = '1'


def nim_random_series(n):
    rang = int(input('Range: ')) + 1
    for i in range(int(input('Times: '))):
        one = random.choice(range(rang))
        two = random.choice(range(rang))
        three = random.choice(range(rang))
        print('input:', (one, two, three))
        a = nimbalance(one, two, three)
        print(a)
        if type(a) == tuple:
            print(nimbalance(a[0], a[1], a[2]))
