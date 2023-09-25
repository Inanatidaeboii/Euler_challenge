def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def find_sum_prime(limit):
    sum_prime = 0
    for i in range(2,limit):
        if is_prime(i):
            sum_prime += i
    return sum_prime

print(find_sum_prime(2000000))


        
