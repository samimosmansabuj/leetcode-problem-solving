# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Example 1:------
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_len = len(nums)
        for i in range(num_len-1):
            for j in range(i+1, num_len):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

two_sum = Solution()
nums = [20, 5, 33,5, 23, 10]
target = 15
print(two_sum.twoSum(nums, target))

