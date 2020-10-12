cnt = 0


def han(n, source, target, auxiliary):
    global cnt
    if n == 1:
        print('Move disk from ' + source + ' to ' + target)
        cnt += 1
    else:
        han(n - 1, source, auxiliary, target)
        print('Move disk from ' + source + ' to ' + target)
        cnt += 1
        han(n - 1, auxiliary, target, source)