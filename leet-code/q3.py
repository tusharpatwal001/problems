# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums = nums1 + nums2
    nums = sorted(nums)
    n = len(nums)
    if n % 2 == 0:
        n1 = n/2
        n2 = (n/2)+1
        print(n1, n2)
        sum = (nums[int(n1-1)] + nums[int(n2-1)])
        print(sum)
        final = sum/2
        return final
    else:
        n1 = (n + 1)/2
        print(n1)
        final = nums[int(n1-1)]
        print(final)
        return final


res = findMedianSortedArrays([1, 2], [3, 4])

print(res)
