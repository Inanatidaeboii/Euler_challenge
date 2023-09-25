def square_list(num1):
    square_num = sum([x**2 for x in range(1,int(num1)+1)])
    return square_num

def sum_square_list(num2):
    sums = sum([x for x in range(1,int(num2)+1)])
    square_of_sum = sums**2
    return square_of_sum

def calculate(num3):
    ans = sum_square_list(num3)-square_list(num3)
    return ans

print(calculate(100))