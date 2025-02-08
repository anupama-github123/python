A=5
k=int(input("enter row to be print:"))
a=[]
for i in range(A):
    b=[None]*(i+1)
    b[0],b[i]=1,1
    if i>1:
        for j in range(1,i):
            b[j]=a[i-1][j]+a[i-1][j-1]
    a.append(b)
print(a[k])

