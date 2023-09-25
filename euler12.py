import math

def get_divisors(n):
    count = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            count += 2
    return count 

i = 1
tri_num = 1
while True:
    if get_divisors(tri_num) > 500:
        break
    i += 1
    tri_num += i

print(tri_num)

