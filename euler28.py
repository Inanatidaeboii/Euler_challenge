# Initialize variables
n = 1  # current number
total = 1  # total sum
side_len = 3  # length of current spiral side

# Continue adding numbers on diagonals until side length is 1001
while side_len <= 1001:
    # Add four numbers on the diagonal
    for i in range(4):
        n += side_len - 1  # increment by side length - 1
        total += n
    side_len += 2  # increment side length by 2

print(total)  # print sum of diagonals
