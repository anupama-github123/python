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