def square(number):
    x = [number] 
    for i in range(64):
        if i!=0:
            x.append(x[i-1]*2)
    return x
def total(number):
    total = sum(square(number))
    return total

number = 1
print(len(square(number)))
print(total(number))

