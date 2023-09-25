def proper_divisors(n):
    divisors = [1]
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i :
                divisors.append(n//i)
    return divisors

def is_abundant(n):
    return sum(proper_divisors(n)) > n

abundant_nums = [x for x in range(1,28124) if is_abundant(x)]

abundant_sums = set()
for i in range(len(abundant_nums)):
    for j in range(i , len(abundant_nums)):
        s = abundant_nums[i] + abundant_nums[j]
        if s > 28123:
            break
        abundant_sums.add(s)

non_abundant_sums = set(range(1,28124)) - abundant_sums

print(sum(non_abundant_sums))