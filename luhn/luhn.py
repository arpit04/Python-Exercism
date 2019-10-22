def addition(n):
    if n%2 == 0:
        return n + n
    else:
        return n
def getSum(r): 
    sum = 0
    while (r != 0):
      
        sum = sum + int(r % 10) 
        r = int(r/10) 
      
    return sum
def mod(total):
    x = total % 10
    if x == 0:
        return print("Valid NUmber")
    else:
        return print("Invalid NUmber")

n = (1,2,3,4,5,6)
result = map(addition, n)
res = list(result)
string = ''.join(map(str, res))
r = int(string)
print(r)

total = getSum(r)
print(mod(100))