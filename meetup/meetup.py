from datetime import datetime, date
import calendar

def get_day(year, month, day_of_week, mod):
    week = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
					"Friday": 4, "Saturday": 5, "Sunday": 6}
    cal = calendar.Calendar()
    date_week = []

    for i in cal.itermonthdays2(year, month):
        if i[0] != 0 and i[1] == week[day_of_week]:
            date_week.append(i)
    if mod != 6:
        return date_week[mod][0]
    else:
        for j in date_week:
            if j[0] in range(13, 20):
                return j[0]

    raise ValueError("That combination doesn't exist.")

def meetup_day(year, month, day_of_week, m):
	# Days that end in 'teenth': 13, 14, 15, 16, 17, 18, 19

    mod_limit = {"first": 0, "second": 1, "third": 2, "fourth": 3, "fifth": 4,
					"last": -1, "teenth": 6}

    return date(year, month, get_day(year, month, day_of_week, mod_limit[m]))

'The first Monday of January 2019'
'The third Tuesday of January 2019'
'The wednesteenth of January 2019'
'The last Thursday of January 2019'

year = 2019
month = 9
day_of_week = 'Monday'
mod = 6
m = "first"
#print(get_day(year, month, day_of_week, mod))
print("the correct meetup date is",meetup_day(year, month, day_of_week, m))
