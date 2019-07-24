# Problem: You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.
#          We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
#Example: [13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.
#         [13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.
#
#Approach:   You only need to search for the element in the array that is decreasing, i.e. nums[i] > nums[i + 1].
#            If you find more than one such elements, return False; if you cannot find one, return True.
#            Then try to find out whether the array can be no-decreasing if you change the value of nums[i] or nums[i + 1]. It can be easily done by one line:
#            return ((nums[i - 1] <= nums[i + 1]) or (nums[i - 2] <= nums[i]))


def checkPossibility(self, nums):
        c = 0  # count for the number of decreasing elements
        p = 0  # place of the decreasing element
        for i in range(len(nums) - 1):
            if(nums[i] > nums[i + 1]):
                c += 1
                p = i + 1
        if c == 0:
            return True
        elif c > 1:
            return False
        else:
            if p == 1 or p == len(nums) - 1:   # corner case
                return True
            else:
                return ((nums[p - 1] <= nums[p + 1]) or (nums[p - 2] <= nums[p]))
