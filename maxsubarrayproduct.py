def maxSubarrayProduct(arr,n):
    result=arr[0]
    for i in range(n):
        mul=arr[i]
        for i in range(i+1,n):
            result=max(result,mul)
            mul*=arr[j]
    return max(result,mul)




def maxSubarraySum(arr,n):  #kadane algorithm
    csum=arr[0]
    osum=arr[0]
    for i in range(len(arr)):
        if(csum>=0):
            csum+=arr[i]
        else:
            csum=arr[i]
        if(csum>osum):
            osum=csum
    return osum
