max_length = 0
max_starting_number = 0

for starting_number in range(1000000,1,-1):
    length = 0
    n = starting_number
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        length += 1

    if length > max_length:
        max_length = length
        max_starting_number = starting_number

print(max_starting_number)

    





