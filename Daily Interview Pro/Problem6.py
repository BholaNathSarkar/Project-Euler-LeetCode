#Problem: Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x.
#         Return -1 if the target is not found.
# Example:
# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]
# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]


class Solution:
    def searchRange(self, nums, target):

        bound=[]
        for i in range(len(nums)):
            if nums[i] == target:
                bound.append(i)
                break

        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                bound.append(j)
                break
        if(len(bound) != 2):
            bound=[-1,-1]

        return bound

arr=[1,3,3,5,7,8,9,9,9,15]
target=9
print(Solution().searchRange(arr,target))
