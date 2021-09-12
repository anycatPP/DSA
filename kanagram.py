

def kanagram(str1,str2,k):
    if str1!=str2:
        return False
    map={}
    for i in len(str1):
        ch=str1[i]
        map.put(ch,map.get(ch)+1)
    for i in len(str2):
        ch2=str2[i]
        if(map.get(ch)>0):
            map.put(ch,map.get(ch)-1)
    count=0
    for ch in map:
        count+=map.get(ch)
    if count>k:
        return False
    else:
        return True
    

print(kanagram('what','the',3))