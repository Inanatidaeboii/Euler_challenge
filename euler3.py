def find_max_prime(limit):
    i = 2
    while i*i <= limit:
        if limit % i != 0:
            i += 1
        else:
            limit //= i
    return limit    

print(find_max_prime(600851475143))  
