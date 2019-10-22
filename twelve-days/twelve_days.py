def recite(days):
    daynum = int(input('What day of Christmas is it? '))

    for i in range(daynum - 1, -1, -1):
        if i == daynum - 1:
            print("On the {} day of Christmas my true love gave to me: ".format(days[i][0]))
        
        if i == 0 and daynum != 1: # if it's the first day and there isn't only 1 day
            print("And ", end='')
        
        print(days[i][1])


if __name__ == "__main__":
    days = (('first', 'A Partridge in a Pear Tree'),
           ('second', 'Two Turtle Doves'),
           ('third', 'Three French Hens'),
           ('fourth', 'Four Calling Birds'),
           ('fifth', 'Five Golden Rings'),
           ('sixth', 'Six Geese a Laying'),
           ('seventh', 'Seven Swans a Swimming'),
           ('eighth', 'Eight Maids a Milking'),
           ('ninth', 'Nine Ladies Dancing'),
           ('tenth', 'Ten Lords a Leaping'),
           ('eleventh', 'Eleven Pipers Piping'),
           ('twelfth', 'Twelve Drummers Drumming'))
    recite(days)
