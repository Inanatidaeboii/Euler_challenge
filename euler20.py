fact = 1
for i in range(1,101):
    fact = fact * i
ans = 0
for j in str(fact):
    ans += int(j)
print(ans)
