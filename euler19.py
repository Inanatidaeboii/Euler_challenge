# import datetime

# count = 0
# for year in range(1901, 2001):
#     for month in range(1, 13):
#         if datetime.date(year, month, 1).weekday() == 6:
#             count += 1

# print(count)

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def count_sundays_on_first_of_month():
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    current_day_of_week = 2 # 1 Jan 1901 is a Tuesday
    count = 0
    
    for year in range(1901, 2001):
        for month in range(0, 12):
            days = days_in_month[month]
            if month == 1 and is_leap_year(year):
                days += 1
            
            if current_day_of_week == 0:
                count += 1
            
            current_day_of_week = (current_day_of_week + days) % 7
    
    return count

print(count_sundays_on_first_of_month())

