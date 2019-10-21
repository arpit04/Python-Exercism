def encode(string):
    count = 1
    s = ''
    for i in range(len(string)):
        if i == (len(string)-1):
            if count!=1:
                s+=str(str(count)+string[i])
                count = 1
            else:
                s+=str(string[i])
                count = 1
        else:
            if i!=(len(string)-1) and string[i] == string[i+1]:
                count += 1
            else:
                if count!=1:
                    s+=str(str(count)+string[i])
                    count = 1
                else:
                    s+=str(string[i])
                    count = 1
    return s

def decode(string):
    new = encode(string)
    res = ''
    counter_len = 0
    for i in range(len(new)):
        c = new[i]
        if c.isdigit():
            counter_len += 1
        else:
            count = int(new[i-counter_len: i] or 1)
            res += c * count
            counter_len = 0
    return res

string = 'awwwwrrrrxttttpppppm'
print("Your Raw String is : ",string)
print("Encoded String : ",encode(string))
print("Decoded String is : ",decode(string))
