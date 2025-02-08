number=int(input("enter a number:"))
rev_number=0
if number <0:
    print('error')
else:
    while number>0:
        digit=number%10
        rev_number=rev_number*10+digit
        number=number //10
print("")