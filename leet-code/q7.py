# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    ls1 = []
    for i in range(len(nums)):
        if nums[i] in ls1:
            return True
        else:
            ls1.append(nums[i])
            print(ls1)
    return False


print(containsDuplicate([1, 2, 3, 4]))
