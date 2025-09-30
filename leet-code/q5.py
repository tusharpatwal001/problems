# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

from typing import List


def singleNumber(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        print(f"index value: {i}")
        var = nums[i]
        if nums.count(var) > 1:
            print(f"{var} is present more than once in {nums}")
            pass
        else:
            return var


print(singleNumber([1, 0, 1]))
