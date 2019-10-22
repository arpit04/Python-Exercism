def convert(number):
    if number % 3 == 0:
        print(str("pling"))
    if number % 5 == 0:
        print(str("plang"))
    if number % 7 == 0:
        print(str("plong"))

# Driver code 
if __name__ == "__main__": 
    # input goes here 
    number = 30
    # Calling function 
    convert(number)
