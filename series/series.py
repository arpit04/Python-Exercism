def slices(string):
    l = input("Enter Length Of Series : ")
    length = int(l)
    for i in range(len(string)-(length-1)):
        print(string[i:i+length])
    return string
    
string = '12345678'
print("Your Raw String : ",slices(string))
