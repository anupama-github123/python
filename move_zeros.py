A=list(map(int,input("enter numbers:").split()))
mylist=[]
mylist1=[]
mylist2=[]
for num in A:
    if(num == 0):
        mylist2.append(num)
    else:
        mylist1.append(num)
        mylist=mylist1 + mylist2
print( mylist)