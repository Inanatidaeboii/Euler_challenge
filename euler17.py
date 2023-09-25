def nums_letter(n):
    ones = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    if n == 1000:
        return len('onethousand')
    elif n >= 100:
        if n%100 == 0:
            return len(ones[n // 100])+len('hundred')
        else:
            return len(ones[n // 100])+len('hundred') + len('and') + nums_letter(n%100)
        
    elif n >= 20:
        return len(tens[n//10]) + nums_letter(n%10)
    else:
        return len(ones[n])
    
totals_letters = sum(nums_letter(i) for i in range(1,1001))
print(totals_letters)