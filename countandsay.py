
def countAndSay(n):
    if n==1:
        return "1"
    return count(countAndSay(n-1))
    
def count(s):
    c=s[0]
    count=1
    res=""
    for char in s[1:]:
        if char==c:
            count+=1
        else:
            res=res+str(count)+c
            c=char
            count=1
    res=res+str(count)+c
    print(res)
    return res

print(countAndSay(5))