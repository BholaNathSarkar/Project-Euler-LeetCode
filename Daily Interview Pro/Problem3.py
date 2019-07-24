# Problem:   Given a string, find the length of the longest substring without
#            repeating characters.
#
# Approach: Count only indexes. Basically we do not need to save any elements, or
#           something. What we need � is once we found element, which makes our
#           string not unique � find last occurrence of this char, and calculate length of
#           the string between current pointer AND last occurrence of the char + 1.
#
#           Let�s take an example of string: abcabc
#             We are starting from index = 0. Once we read the char => we are adding it
#             to the hashtable with index = 0. b with index 1. c with index 2. Then we�ve
#             encountered character a again. it is obvious that unique string starts from
#             the first location of a + 1: a->bca->bc and length 3.
#              Then after we meet b again, we are moving again: ab->cab->abc. And so on.
#
#          So, for us � main thing is to save last occurrence of each symbol,
#          which helps us to calculate length of the unique string.

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        if(len(s)==0):
            return 0
        start=maxLength=0

        usedChars={}      ##Dictionary which will contain letters as, usedChars={'a':0,'b':1,'c':2}
        for i in range(len(s)):
            if(s[i] in usedChars and start<=usedChars[s[i]]):
                start=usedChars[s[i]]+1
            else:
                maxLength=max(maxLength, i- start + 1)
            usedChars[s[i]]=i
        return maxLength
print(Solution().lengthOfLongestSubstring("abcdefab"))
