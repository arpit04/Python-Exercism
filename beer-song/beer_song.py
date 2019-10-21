for i in range(99, 0, -1):
    if i == 2:
        print(str(i)+" bottles of beer on the wall, "+str(i)+" bottles of beer.\nTake one down and pass it around, "+str(i-1)+" bottle of beer on the wall.\n")
    elif i == 1:
        print(str(i)+" bottle of beer on the wall, "+str(i)+" bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n")

        print("no more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n")
    else:
        print(str(i)+" bottles of beer on the wall, "+str(i)+" bottles of beer.\nTake one down and pass it around, "+str(i-1)+" bottles of beer on the wall.\n")