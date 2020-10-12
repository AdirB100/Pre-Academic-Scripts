def sub_encrypt(plaintext, alphabet, shuffled):
    ciphertext = ''
    for char in plaintext:
        if char in alphabet:
            ciphertext += shuffled[alphabet.find(char)]
        else:
            ciphertext += char
    return ciphertext


def sub_decrypt(ciphertext, alphabet, shuffled):
    return sub_encrypt(ciphertext, shuffled, alphabet)
