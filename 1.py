def differnece(arr,n):
    d1=0
    d2=0
    for i in range(0,n):
        d1=d1+arr[i][i]
        d2=d2+arr[i][n-i-1]
    return abs(d1-d2)

n=3
arr=[[11,2,4],[4,5,6],[10,8,-12]]
print(differnece(arr,n))







