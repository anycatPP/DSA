from typing import List


def longestcommonprefix(self,str:List[str])->str:
    if len(str)==0:
        return ("")
    if len(str)==1:
        return (str[0])
    pref=str[0]
    plen=len(pref)
    for s in str[1:]:
        while pref!=s[0:plen]:
            pref=pref[0:(plen-1)]
            plen-=1
            if plen==0:
                return ("")
    return pref

print(longestcommonprefix(str=['what','the ','fuck']))