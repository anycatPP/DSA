def subArraySum(arr,n,sum_):
    for i in range(n):
        curr_sum=arr[i]
        j=i+1
        while j<=n:
            if curr_sum==sum:
                print('sum found between ')
                print(i,j-1)
                return 1
            if curr_sum>=sum_ or j==n:
                break
            curr_sum=curr_sum+arr[j]
            j+=1
    print('no subarray found')
    return 0
# efficient approach using slidiing window algorithm
def subArraySum(arr,n,sum_):
    curr_sum=arr[0]
    start=0
    i=1
    while i<=n:
        while curr_sum>sum_ and start<i-1:
            curr_sum=curr_sum-arr[start]
            start+=1
        if curr_sum==sum_:
            print(start,i-1)
            return 1
        if i<n:
            curr_sum=curr_sum+arr[i]
        i+=1
    print('no subarray found')
    return 0
