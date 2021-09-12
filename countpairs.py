def getPairsCount(arr,n,sum):
    count=0
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==sum:
                count+=1
    return count


#efficent solution
# a better solution is possible in O(n) time since
# create a map to store frequency of each number in the array 
# in the next traversal for every element check if it can be combined 
# with any ohte relement other than itself to give the desired sum
#increment the counter accordingly
# after completion of second traversal we'd have twice the required value 
# stored in counter because every pari is counted two times hence divide by z
# 2 and return 


import sys

def getPairsCount(arr,n,sum):

    unordered_map={}
    count=0
    for i in range(n):

        if sum-arr[i] in unordered_map:

            count+=unordered_map[sum-arr[i]]
        if arr[i] in unordered_map:
            unordered_map[arr[i]]+=1
        else:
            unordered_map[arr[i]]=1
    return count
    