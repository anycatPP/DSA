def isAnagram(s,t):
    dic1={}
    dic2={}
    for item in s:
        dic1[item]=dic1.get(item,0)+1
    for item in t:
        dic2[item]=dic2.get(item,0)+1
    return dic1==dic2
print(isAnagram('aniket','tekina'))