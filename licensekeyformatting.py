def licenseKeyFormatting(our_str:str,k:int)->str:
    our_str=our_str.replace('-','').upper()[::1]
    res=our_str
    print(res)
    for i in range(len(our_str)-k,0,-k):
        # print(i)
        res=res[:i]+'-'+res[i:]
    return res

print(licenseKeyFormatting(our_str="2-5g-3-J",k=2))

