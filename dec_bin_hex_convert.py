def dec2bin(dec_num):
    if dec_num == 0:
        return 0
    bin_num = ''
    while dec_num > 0:
        bin_num = str(dec_num % 2) + bin_num
        dec_num //= 2
    return int(bin_num)


def bin2dec(bin_num):
    str_bin_num = str(bin_num)
    dec_num = 0
    for j in range(len(str_bin_num)):
        dec_num += int(str_bin_num[j]) * 2 ** ((len(str_bin_num) - 1) - j)
    return dec_num


def dec2hex(dec_num):  # receives integer, returns string
    if dec_num == 0:
        return '0'
    hex_str = ''
    while dec_num > 0:
        if 0 <= dec_num % 16 <= 9:
            hex_str = str(dec_num % 16) + hex_str
        else:
            hex_str = 'ABCDEF'[(dec_num % 16) - 10] + hex_str
        dec_num //= 16
    return hex_str


def hex2dec(hex_str):  # receives string, returns integer
    hex_str = str(hex_str)
    ls = []
    for char in hex_str:
        if char in 'ABCDEF':
            char = 'ABCDEF'.find(char) + 10
        ls.append(int(char))
    dec_num = 0
    for j in range(len(ls)):
        dec_num += ls[j] * 16 ** ((len(ls) - 1) - j)
    return dec_num