def text_char_analyzer(path2txt):
    from string import digits, punctuation, whitespace
    file = open(path2txt)
    try:
        r = file.read()
        for i in punctuation + ' ' + whitespace + digits:
            r = r.replace(i, '')
        r = r.lower()
        dic = {}
        for char in r:
            dic[char] = dic.get(char, 0) + 1
        for let in sorted(dic, key=dic.get, reverse=True):
            print('{0} -> {1}%'.format(let, round(100 * dic[let] / sum(dic.values()), 2)))
    finally:
        file.close()


def text_word_analyzer(path2txt):
    from string import punctuation, digits
    file = open(path2txt)
    try:
        content = file.read()
        for char in punctuation + "\t\n\r\x0b\x0c":
            content = content.replace(char, ' ')
        content = content.lower()
        for dig in digits:
            content = content.replace(dig, '')
        dic = {}
        for word in content.split():
            dic[word] = dic.get(word, 0) + 1
        for a_word in sorted(dic, key=dic.get, reverse=True):
            print(f'{a_word} -> {round((100 * dic[a_word] / sum(dic.values())), 7)}')
    finally:
        file.close()
