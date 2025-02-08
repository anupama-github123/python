num=int(input("enter range:"))
mylist=[]
for i in range(num):
    value=int(input("enyer the values:"))
    mylist.append(value)
    sum=min(mylist)+max(mylist)
print("sum:",int(sum))