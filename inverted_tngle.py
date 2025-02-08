num=int((input("enter the number:")))
for i in range(1,num):
    for j in range(num-i):
        print(' ',end='')
    for j in range(2 * i-1):
         print(' * ',end=' ')
    print()