# find the first repeating element in an array of integers

def printFirstRepeating(arr,n):
    Min=-1
    myset=dict()
    for i in range(n-1,-1,-1):
        if arr[i] in myset.keys():
            Min=i
        else:
            myset[arr[i]]=1
    if(Min!=-1):
        print("the first repeating element is",arr[min])
    else:
        print('there are no repeating elements')
        