# author: YANG CUI
"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once.
Find that single one.
Note:
The algorithm should have a linear runtime complexity. Implement it without using extra memory.
"""

# idea taken from: https://leetcode.com/problems/single-number-ii/discuss/340185/Python-5-line-bit-operation-92-70

# ~ is the bitwise inversion operator
# The bit-wise inversion of x is -(x+1)

def singleNumber_bitwise(nums):
    """
    Approach: bit manipulations (XOR) ^
    Concept: If we take XOR of zero and some bit, it will return that bit. If we take XOR of two same bits, it will return 0
    :param nums: input list of numbers containing only 1 element that appeared once
    :return: that element
    :time complexity: O(n)
    :space complexity: O(1)
    """
    result1 = 0
    result2 = 0
    for elem in nums:
        result1 = (result1 ^ elem) & (~result2)
        result2 = (result2 ^ elem) & (~result1)
    return result1

# print(singleNumber_bitwise([0,1,0,1,0,1,99]))
