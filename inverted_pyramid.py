num=int((input("enter the number:")))
for i in range(1,num):
    for j in range(i):
        print(' ',end=' ')
    for j in range(num - i):
         print('*',end=' ')
    print()