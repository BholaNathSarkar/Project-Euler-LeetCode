"""
Problem Statement:
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).
Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.
Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
"""
"""
Approach:
If second element from last is 0: it is always true
if second element from last is 1: count the number of continuous 1's before last zero.
if the count turns out to be odd--false
otherwise--true
"""
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i=len(bits)-2
        c=0
        if(bits[i]==0):
            return True
        else:
           while(bits[i]==1 and i>=0):
              c=c+1
              i=i-1
           if(c%2==0):
            return True
           else:
                return False
