long_months = [1, 3, 5, 7, 8, 10, 12]
short_months = [4, 6, 9, 11]
leap_months = [2]

def dateIsBefore(year_one, month_one, day_one, year_two, month_two, day_two):
    if year_one < year_two:
        return True
    if year_one == year_two:
        if month_one < month_two:
            return True
        if month_one == month_two:
            if day_one < day_two:
                return True
    return False

def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    if month in long_months:
        return 31
    if month in short_months:
        return 30
    if month in leap_months:
        if isLeapYear(year) == True:
            return 29
        else:
            return 28

def getNextDay(year, month, day):
    if day < daysInMonth(year, month):
        day += 1
        return year, month, day
    else:
        if day == daysInMonth(year, month) and month == 12:
            year += 1
            month = 1
            day = 1
            return year, month, day
        else:
            month += 1
            day = 1
            return year, month, day

def daysBetweenDates(year_one, month_one, day_one, year_two, month_two, day_two):
    assert dateIsBefore(year_one, month_one, day_one, year_two, month_two, day_two)
    days = 0
    while dateIsBefore(year_one, month_one, day_one, year_two, month_two, day_two):
        days += 1
        year_one, month_one, day_one = getNextDay(year_one, month_one, day_one)
    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

if __name__ == '__main__':
    test()
