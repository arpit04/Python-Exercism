vowel = ['a','e','i','o','u']
def translate(text):
    if text[0:2] == 'xr' or text[0:2] == 'yt':
        return text+"ay"
    elif text[0] in vowel:
        return text+"ay"
    else:
        for i in range(len(text)):
            if text[i] == 'y' and i!=0:
                return text[i:]+""+text[0:i]+"ay"
        x = ((len(text)) - len(text)//2)
        consonant = text[len(text)//2:]+""+text[0:(len(text)//2)]+"ay"
        return consonant
text = input("Enter Word :")
print(translate(text))