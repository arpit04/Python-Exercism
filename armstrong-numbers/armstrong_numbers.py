def is_armstrong_number(n):
    x = []
    for i in range(len(n)):
        m = int(n[i])**len(n)
        x.append(m)
    s = sum(x)
    print("after itration : ",s)
    if s == int(n):
        print(n,"is armstrong number")
        return True
    else:
        print(n,"is not armstrong number")
        return False 
n = input("Enter number : ")
print(is_armstrong_number(n))


