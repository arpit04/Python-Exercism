from string import ascii_lowercase

def encode(plain_text):
    ct = ''
    rev = ''.join(reversed(ascii_lowercase))
    for i in range(len(plain_text)):
        for j in range(len(ascii_lowercase)):
            if plain_text[i] == ascii_lowercase[j]:
                ct = ct+rev[j]
    return ct

def decode(ciphered_text):
    pt = ''
    rev = ''.join(reversed(ascii_lowercase))
    for i in range(len(ciphered_text)):
        for j in range(len(ascii_lowercase)):
            if ciphered_text[i] == ascii_lowercase[j]:
                pt = pt+rev[j]
    return pt

plain_text = 'arpit'
print("Plain Text :",plain_text)
ciphered_text = encode(plain_text)
print("Encoded Text :",encode(plain_text))
print("Decoded Text :",decode(ciphered_text))
