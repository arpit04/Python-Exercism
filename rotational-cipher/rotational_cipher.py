from string import ascii_lowercase
ct = []
str1 = ""

def rotate(text, key):
    index = 0
    for j in range(len(text)):
        for i in range(len(ascii_lowercase)):
            if ascii_lowercase[i] == text[j]:
                if (i+key) > 25:
                    new_key = (i+key)-26
                    ct.append(ascii_lowercase[new_key])
                else:
                    ct.append(ascii_lowercase[i+key])
    return str1.join(ct)
text = 'the'

# ------> Key must be between 1 to 25 <-----
key = 13
print(rotate(text, key))

