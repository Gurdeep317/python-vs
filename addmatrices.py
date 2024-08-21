a=[[2,5,6],
   [3,7,8],
   [0,8,6]]

b=[[3,5,6],
   [1,3,4],
   [4,3,5]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result [i][j]= a[i][j]+b[i][j]

for r in result:
    print(r)