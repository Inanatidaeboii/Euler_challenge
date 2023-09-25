def gcd(a,b):
    while b:
        a , b = b , a % b
    return a

def find_smallest_divisible(limit):
    ans = 1
    for i in range(1 , limit + 1):
        ans *= i // gcd(i,ans)
    return ans
    
print(find_smallest_divisible(20))
        