my_list=[]
num=int(input("enter the number:"))
for _ in range(num):
    value=int(input("enter the numbers:"))
    my_list.append(value)
target=int(input("enter the target:"))
found =False
for i in range(len(my_list)):
    if target == my_list[i]:
        found=True
        break
if found:
    print("targt found")
else:
    print("target was not found")