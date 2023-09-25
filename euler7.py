def find_prime(n):
        if n <= 1:
            return False
        for i in range(2,int((n**0.5))+1):
            if n % i == 0:
                return False
        return True
def find_max_prime(n):
    count = 0
    nums = 2
    while count < n:
        if find_prime(nums):
            count += 1
        nums += 1
    return nums - 1

print(find_max_prime(10001))
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def nth_prime(n):
#     count = 0
#     num = 2
#     while count < n:
#         if is_prime(num):
#             count += 1
#         num += 1
#     return num - 1

# print(nth_prime(10001))
