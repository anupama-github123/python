row_size=int(input("enter th row size:"))
clm_size=int(input("enter th column size:"))
matrix=[]
print("enter the matrix elements:")
for i in range(row_size):
    a=[]
    for j in range(clm_size):
        a.append(int(input()))
    matrix.append(a)
print("\n----MATRIX----")
for i in range(row_size):
    for j in range(clm_size):
        print(matrix[i][j],end="\t")
    print()
r=len(matrix)
c=len(matrix[0])
min_row=0
max_row=r-1
min_clm=0
max_clm=c-1
print("\n---spral order---")
spiral=[]
while (len(spiral)< r*c):
    for i in range(min_clm,max_clm)+1:
        spiral.append(matrix[min_row][i])
    min_row=min_row+1
    for i in range(min_row,max_row+1):
        spiral.append(matrix[i][max_clm])
    max_clm=max_clm-1

print(spiral)
print()

