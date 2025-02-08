
mylist=[]
mylist2=[]
mylist3=[]
while True:
    num=input("enter the number:")
    if num == 'stop':
        break
    elif (num == '0'):
        mylist.append(num)
    else:
        mylist2.append(num)
mylist3=mylist+mylist2
print("new array:",mylist3)
