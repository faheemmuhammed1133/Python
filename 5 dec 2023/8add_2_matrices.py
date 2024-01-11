# add to matrices
x=[[2,5,4],[1,3,9],[7,6,2]]
y=[[1,8,5],[7,3,6],[4,0,8]]
r=[[1,2,3],[2,3,4],[3,4,5]]
for i in range(len(x)):
    for j in range(len(x)):
        r[i][j]=x[i][j]+y[i][j]
    print(r[i])