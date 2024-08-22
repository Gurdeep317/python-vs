A =[[2,4,6],
    [1,3,5]]
transpose=[[0,0],
           [0,0],
           [0,0]]
for i in range (len(A)):
    for j in range (len(A[0])):
        transpose[j][i]=A[i][j]
for i in transpose:
    print(i)