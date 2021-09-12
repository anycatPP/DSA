def repeatedStringMatch(stringA,stringB):
    count=0
    sb=""
    while len(sb)<len(stringB):
        sb+="".join(stringA)
        count+=1
    if stringB in sb:
        return count
    if stringB in sb.join(stringA):
        return count+1
    return -1