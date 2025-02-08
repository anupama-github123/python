r=int(input("enter the no of rows    : "))
c=int(input("enter the no of columns : "))
mat=[]
print("enter the elements of matrix")
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    mat.append(a)
print("\n----MATRIX----\n")
for i in range(r):
    for j in range(c):
        print(mat[i][j],end="\t")
    print()
r=len(mat)
c=len(mat[0])
mr,mc,mxr,mxc=0,0,r-1,c-1
ar=[]
while(len(ar)<r*c):
    for j in range(mc,mxc+1):
        ar.append(mat[mr][j])
    mr+=1
    for i in range(mr,mxr+1):
        ar.append(mat[i][mxc])
    mxc-=1
    for j in range(mxc,mc-1,-1):
        ar.append(mat[mxr][j])
    mxr-=1
    for i in range(mxr,mr-1,-1):
        ar.append(mat[i][mc])
    mc+=1
print(ar)