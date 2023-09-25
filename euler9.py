for a in range(1,998):
        for b in range(a+1,999):
            c = 1000 - a - b 
            if c>b and a**2 + b**2 == c**2 :
                multiple = a*b*c
                print(multiple,a,b,c)
                break
# for a in range(1, 998):
#     for b in range(a+1, 999):
#         c = 1000 - a - b
#         if a**2 + b**2 == c**2:
#             print(a * b * c,a,b,c)
#             break
