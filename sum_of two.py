my_list=[]
num=int(input("enter the number:"))
for _ in range(num):
    value=int(input("enter the numbers:"))
    my_list.append(value)
sum=int(input("enter a number for sum:"))
found = False
for i in range(num):
    for j in range(i+1,num):
             if my_list[i]+my_list[j] == sum:
                found=True
                print(f"the numbers are{my_list[i]} and {my_list[j]}")
                break
    if found:
        break
if not found:
     print('the numbers are not found')
