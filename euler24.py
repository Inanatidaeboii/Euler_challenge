a, b = 1, 1  # initialize the first two terms
index = 2    # initialize the index to 2 (since we already have F1 and F2)

while len(str(b)) < 1000:
    # generate the next term in the sequence
    a, b = b, a + b
    index += 1

print(index)
