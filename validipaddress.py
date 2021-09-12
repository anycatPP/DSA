def validIPAddress(self,IP):
    def isIPv4(s):
        try:
            return str(int(s))==s and 0<=int(s)<=255
        except :
            return False

    def isIPv6(s):
        try:
            return len(s)<=4 and int(s,16)>=0
        except :
            return False
    
    
    if IP.count(".")==3 and all(isIPv4(i) for i in IP.split(".")):
        return "IPV4"
    if IP.count(":")==7 and all(isIPv4(i) for i in IP.split(":")):
        return "IPV4"
    return "neither"
    