def solution(arr):
    ans=0
    c0=0
    c1=0
    c2=0
    key=(c1-c0)+"#"+(c2-c1)
    map.put(key,1)
    for val in arr:
        if val==0:
            c0+=1
        elif val==1:
            c1+=1
        else:
            c2+=1
        key=(c1-c0)+'#'+(c2-c1)
        if key in map:
            ans+=map.get(key)
            map.put(key,map.get(key)+1)
        else:
            map.put(key,1)
