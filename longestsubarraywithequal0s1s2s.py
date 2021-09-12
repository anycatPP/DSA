def longestsubarraywithequal0and1(arr):
    ans=0
    map={}
    countz=0
    counto=0
    countt=0
    delta10=counto-countz
    delta21=countt-counto
    key=delta21+'#'+delta10
    map.put(key,-1)
    for i in arr:
        if arr[i]==0:
            countz+=1
        elif arr[i]==1:
            counto+=1
        else:
            countt+=1
        delta10=counto-countz
        delta21=countt-counto
        key=delta21+'#'+delta10
        if key in map:
            idx=map.get(key)
            len=i-idx
            if len>ans:
                ans=len
            else:
                map.put(key,i)
