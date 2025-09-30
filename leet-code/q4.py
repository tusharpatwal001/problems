# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.


# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    print("*-*"*20)
    p1 = 0
    p2 = len(s)-1
    while p1 < p2:
        print(f"p1 -> {p1}, p2 -> {p2}")
        s[p1], s[p2] = s[p2], s[p1]
        print(s)
        print()
        p1 += 1
        p2 -= 1
    print("*-*"*20)
    return s


print(reverseString(["h", "e", "l", "l", "o"]))
print(reverseString(["H", "a", "n", "n", "a", "h"]))
