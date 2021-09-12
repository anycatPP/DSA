def isRotated(str1,str2):
    if(len(str1)!=len(str2)):
        return False
    if(len(str1)<2):
        return str1==str2
    clock_rot=""
    anticlock_rot=""
    l=len(str2)
    anticlock_rot=(anticlock_rot+str2[l-2:]+str2[0:1-2])
    