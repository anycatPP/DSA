def lengthOfLongestSubstring(s):
    a_pointer=0
    b_pointer=0
    maxi=0
    sets=set()                                                                  #length of longest substring use 2 pointer approach that is called from
    while(b_pointer<len(s)):                                                     #sliding window algorithm        
        if s[b_pointer] not in sets:
            sets.add(s[b_pointer])
            b_pointer+=1
            maxi=max(len(sets),maxi)
        else:
            sets.remove(s[a_pointer])
            a_pointer+=1
    return maxi

print(lengthOfLongestSubstring('abcabcbb'))
