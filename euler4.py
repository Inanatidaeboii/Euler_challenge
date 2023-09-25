def max_palindrome():
    max_palindrome = 0
    for i in range(100,1000):
        for j in range(100,1000):
            limit = i * j
            if str(limit) == str(limit)[::-1] and limit > max_palindrome:
                max_palindrome = limit
    return max_palindrome

print(max_palindrome())