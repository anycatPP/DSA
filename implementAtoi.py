def atoi(str,i):
    i=0
    res=0
    negative=1
    #whitespace
    MAX_INT=2**31-1
    MIN_INT=2**31
    while i<len(str) and str[i]==' ':
        i+=1
    # +/- symbol
    if i<len(str) and str[i]=='-':
        i+=1
        negative=-1
    elif i<len(str) and str[i]=='+':
        i+=1
#check number 0-9
    checker=set('0124356789')
    while i<len(str) and str[i] in checker:
        res=res*10+int(str[i])
        i+=1
    res=res*negative
#CHECK THE MAX/MIN INT
    if res<0:
        return max(res,MIN_INT)
    return min(res,MAX_INT)
