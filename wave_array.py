a=[1,2,3,4,5]
temp=0
for i in range(0,len(a)-1,2):
    temp=a[i]
    a[i]=a[i+1]
    a[i+1]=temp
print("new array:",a)