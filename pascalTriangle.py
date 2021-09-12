def pascalTriangle(numRows):
    pascal=[[1]*(i+1)for i in range(numRows)]
    # print(pascal)
    for i in range(numRows):
        for j in range(1,i):
            pascal[i][j]=pascal[i-1][j-1]+pascal[i-1][j]
    return pascal

print(pascalTriangle(4))