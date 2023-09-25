# answer = set()
# for i in range(2,99999):
#     fifth_power = str(i)
#     total_fifth_power = sum([int(x)**5 for x in fifth_power])
#     if total_fifth_power == i:
#         answer.add(i)

# print(sum(answer))


def sum_of_digit_powers(n, power):
    # Function to calculate the sum of the given number's digits raised to the specified power
    return sum(int(digit)**power for digit in str(n))

def find_sum_of_numbers(power):
    # Function to find the sum of all the numbers that can be written as the sum of digit powers
    result = 0
    # Iterate through numbers from 2 to an upper limit
    for num in range(2, 10**(power+1)):
        if sum_of_digit_powers(num, power) == num:
            result += num
    return result

power = 5
sum_of_numbers = find_sum_of_numbers(power)
print("The sum of all the numbers that can be written as the sum of fifth powers of their digits is:", sum_of_numbers)



