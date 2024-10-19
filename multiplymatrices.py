# program to multiply two matrices
# taking a and b,two matrices
# using for loop
A=[[1,3,5],
   [2,4,6],
   [7,8,9]]
B=[[1,5,3],
   [4,7,3],
   [0,2,3]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range (len(A)):
    for j in range(len(A[0])):
        result[i][j]=A[i][j]*B[i][j]
for i in result :
    print(i)

