# 169. Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


from collections import Counter
from typing import List


def majorityElement(nums: List[int]) -> int:
    maps = Counter(nums)
    # print(f"maps -> {maps}")
    keys = [i for i in maps.values()]
    ans = max(keys)
    # print(ans)
    for i, j in maps.items():
        # print(f"i -> {i}, j -> {j}")
        if j == ans:
            return i


print(majorityElement([3, 2, 3]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
