def caesar_encrypt(plaintext, k):
    def encrypt_let(char, n):
        if ord(char) not in range(97, 123):
            return char
        if n >= 0:
            n = n % 26
        else:
            n = -((-n) % 26)
        num_char_ord = ord(char) + n
        if num_char_ord in range(97, 123):
            return chr(num_char_ord)
        if n >= 0:
            return chr(num_char_ord - 26)
        return chr(num_char_ord + 26)
    new_st = ''
    for i in plaintext:
        new_st += encrypt_let(i, k)
    return new_st


def caesar_decrypt(ciphertext, k):
    return caesar_encrypt(ciphertext, -k)