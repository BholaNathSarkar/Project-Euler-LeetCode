# Probelem: You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.
# Example: Given [4, 7, 1 , -3, 2] and k = 5,
#          return true since 4 + 1 = 5.
#Solution:
class Solution:
    def two_sum(self,nums,target):
        dict={}
        for i in range(len(nums)):
            n=target-nums[i]
            if n  not in dict:
                dict[nums[i]]=i
            else:
                #return [dict[n],i]
                return True
#Test Program
a=[4,7,1,-3,2]
k=11
print(Solution().two_sum(a,k))
