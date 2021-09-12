
def findFrequency (arr, n, x):
    freq={}
    for item in arr:
        if(item in freq):
            freq[item]+=1
        else:
            freq[item]=1
    print(freq[x])
    return freq[x]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    arr = list (map (int, input ().split ()))
    x = int (input ())
    print (findFrequency (arr, n, x))
    
# } Driver Code Ends
