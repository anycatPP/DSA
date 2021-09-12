def isomorphicString(s,t):
    if (len(s)!=len(t)):
        return False
    map1={}
    map2={}
    for i in range(s):
        ch1=s.charAt(i)
        ch2=t.charAt(i)
        if(ch1 in map1):
            if map1.get(ch1)!=ch2:
                return False
            else:
                if ch2 in map2:
                    return False
                else:
                    map1.put(ch1,ch2)
                    map2.put(ch2,True)
    return True

print(isomorphicString('what','the'))