def find_even_value(limit):
    a,b = 1,2
    result = 0
    while b<=limit:
        if b % 2 == 0:
            result += b
        a , b = b , a + b
    return result

print(find_even_value(4000000))
