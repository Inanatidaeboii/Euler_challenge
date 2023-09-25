d = 1000
checker = 0
for i in range (2,(d+1)):
    recurring_nums = 1 // i
    if recurring_nums > checker:
        checker = recurring_nums

    
print(recurring_nums)