combination = set()
for i in range(2,101):
    for j in range(2,101):
        combination.add(i**j)

sequence = len(sorted(combination))

print(sequence)

