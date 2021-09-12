def longestWord(words):
    words.sort()
    words_set=set([''])
    longest_word=''
    for word in words:
        if word[:-1] in words_set:
            words_set.add(word)
            if len(word)>len(longest_word):
                longest_word=word
    return longest_word

print(longestWord(['aniket','anikett']))