
#Naive Solution -JavaScript O(n^2) --it returns numbers
#For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.

function twoSum(arr, S) {
  var sums = [];

  for (var i = 0; i < arr.length; i++) {
    // check each other element in the array
    for (var j = i + 1; j < arr.length; j++) {
    // determine if these two elements sum to S
      if (arr[i] + arr[j] === S) {
        sums.push([arr[i], arr[j]]);
      }
}
}
 // return all pairs of integers that sum to S
  return sums;
}


#Problem : Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#          You may assume that each input would have exactly one solution, and you may not use the same element twice.
#example:  Given nums = [2, 7, 11, 15], target = 9,
#          Because nums[0] + nums[1] = 2 + 7 = 9,
#          return [0, 1].

#Faster Solution O(n)  --this solution returns index
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            n=target-nums[i]
            if n not in dict:
                dict[nums[i]]=i
            else:
                return [dict[n],i]
