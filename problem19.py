

def nextDate(day, month, year):
    day += 1
    if month in thirtyDays:
        if day > 30:
            day = 1
            month += 1
    elif month == 2:
        if year % 4 == 0:
            if day > 29:
                day = 1
                month += 1
        else:
            if day > 28:
                day = 1
                month += 1
    else:
        if day > 31:
            day =1
            month += 1
    if month > 12:
        month = 1
        year += 1
    return day, month, year



if __name__ == '__main__':

    thirtyDays = [4,6,9,11]

    dayOfTheWeek = 1
    day = 1
    month = 1
    year = 1901

    count = 0
    while year < 2001:
        dayOfTheWeek += 1
        dayOfTheWeek = dayOfTheWeek % 7
        day, month, year = nextDate(day, month, year)
        if dayOfTheWeek == 6:
            if day == 1:
                count += 1

    print(count)
