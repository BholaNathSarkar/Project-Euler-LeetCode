# Problem: Given a list of numbers, where every number shows up twice except for one number, find that one number.
# Example: Input: [4, 3, 2, 4, 1, 3, 2]
#         Output: 1
#Challenge: Find a way to do this using O(1) memory.
#O(1) means constant average memory use, regardless the size of your input

#Solution 1:

class Solution:
    def find_non_duplicate(self,arr):
        dict={}
        for i in range(len(arr)):
            if arr[i] not  in dict:
                dict[arr[i]]=1
            else:
                dict[arr[i]]=2
        for n,count in dict.items():
           if(count == 1):
              return n
#Test Program
a=[1,4,3,2,4,3,2]
print(Solution().find_non_duplicate(a))

#Solution 2:Better Approach  :Time complexity of this solution is O(n) ,Space Complexity:O(1)

#The best solution is to use XOR. XOR of all array elements gives us the number with single occurrence..The idea is based on following two facts.
#   a) XOR of a number with itself is 0.
#   b) XOR of a number with 0 is number itself.
#Let us consider the above example. Let ^ be xor operator as in C and C++.
#res = 7 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4
#Since XOR is associative and commutative, above expression can be written as:
#res = 7 ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)
#    = 7 ^ 0 ^ 0 ^ 0
#    = 7 ^ 0
#    = 7

class Solution2:
    def find_Single(self,arr):
        result=arr[0]
        for i in range(1,len(arr)):
            result=result ^ arr[i]
        return result
#Test Program
a=[2, 3, 5, 4, 5, 3, 4]
print(Solution2().find_Single(a))
