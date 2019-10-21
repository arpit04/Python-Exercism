def leap_year(year):
    if int(year)%4 == 0:
        if int(year)%100 == 0:
            if int(year)%400 == 0:
                return "is leap year"
            return "is not leap year"
        return "is leap year"
    else:
        return "is not leap year"
year = input("Enter Year :")
print(leap_year(year))