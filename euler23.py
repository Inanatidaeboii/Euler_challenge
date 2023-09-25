import itertools

digit = list(range(10))

permutation = sorted(itertools.permutations(digit))

print(''.join(map(str,permutation[999999])))

# def permute(digits, l, r):
#     if l == r:
#         # base case: we have reached the end of the list
#         yield digits
#     else:
#         # recursive case: generate permutations by swapping elements
#         for i in range(l, r+1):
#             digits[l], digits[i] = digits[i], digits[l]
#             yield from permute(digits, l+1, r)
#             digits[l], digits[i] = digits[i], digits[l]

# # create a list of digits from 0 to 9
# digits = list(range(10))

# # generate all permutations of the digits and sort them in lexicographic order
# permutations = sorted(permute(digits, 0, len(digits)-1))

# # print the millionth permutation (indexed at 0)
# print(''.join(map(str, permutations[999999])))