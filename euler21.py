def sum_of_divisible(n):
    divisible = [1]
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            divisible.append(i)
            if i != n //i :
                divisible.append(n//i)

    return sum(divisible)

sum_of_divisors = set()

for a in range(2,10000):
    b = sum_of_divisible(a)
    if a != b and sum_of_divisible(b) == a:
        sum_of_divisors.add(a)
        sum_of_divisors.add(b)

print(sum(sum_of_divisors))







