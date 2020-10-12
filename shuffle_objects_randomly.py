def shuffle(arg):
    import random
    if type(arg)==list:
        random.shuffle(arg)
        return arg
    if type(arg)==str:
        arg=list(arg)
        random.shuffle(arg)
        b=''
        for i in arg:
            b+=i
        return b
    if type(arg)==range:
        arg = list(arg)
        random.shuffle(arg)
        return arg
    if type(arg)==int:
        arg= list(str(arg))
        random.shuffle(arg)
        b = ''
        for i in arg:
            b += i
        return int(b)
