my_list=[]
num=int(input("enter the number:"))
for _ in range(num):
    value=int(input("enter values:"))
    my_list.append(value)
target=("enter the mid value:")
if num<0:
    mid=(high+low)/2
    if(mid>target):
        mid =high
    else:
        mid=low
print("the trget found",mid)

