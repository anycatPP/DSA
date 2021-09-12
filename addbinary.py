def addBinary(a,b):
    sb=''
    i=len(a)-1
    j=len(b)-1
    carry=0
    while i>=0 or j>=0:
        sum=carry
        if i>=0:
            sum+=a[i]-'0'
        if j>0:
            sum+=b[i]-'0'
        sb.append(sum%2)
        carry=sum/2
        i-=1
        j-=1
    if carry!=0:
        sb.append(carry)
    return sb.reverse()

