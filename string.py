# # reverse only letters 
# def reverseOnlyLetters(S:str)->str:
#     S=list(S)
#     l,r=0,len(S)-1
#     while l<r:
#         if S[l].isalpha() and S[r].isalpha():
#             S[l],S[r]=S[r],S[l]
#             l+=1
#             r-=1
#         else:
#             if not S[l].isalpha():
#                 l+=1
#             if not S[r].isalpha():
#                 r-=1
#         return ''.join(S)




# print(reverseOnlyLetters(S='what-the--fuck'))
# reverse only words in given string
# def reverseWords(self,s):
#     s=list(" ",join(s.split()))[::-1]
#     i=0
#     while i<len(s):
#         start=i
#         while i<len(s) and not s[i].isspace():
#             i+=1
#         self.reverse(s,start,i-1)
#         i+=1
#     return "".join(s)
# def reverse(self,s,i,j):
#     while i<j:
#         s[i]=s[j]
#         s[j]=s[i]
#         i+=1
#         j-=1



def longestcommonprefix(str):
    if str==0:
        return ""
    prefix=str[0]
    for i in range(len(str)):
        while str[i].index(prefix)!=0:
            prefix=prefix.substr(0,prefix.length()-1)
    return prefix

print(longestcommonprefix(['what ','the fuck','whisdf']))
