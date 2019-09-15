# author: YANG CUI
"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once.
linear time and constant space
"""
import collections
def singleNumber_xor(nums):
    """
    Approach: bit manipulations (XOR) ^
    Concept: If we take XOR of zero and some bit, it will return that bit. If we take XOR of two same bits, it will return 0
    :param nums: input list of numbers containing only 1 element that appeared once
    :return: that element
    :time complexity: O(n)
    :space complexity: O(1)
    """
    result = 0
    for elem in nums:
        result ^= elem
    return result

# singleNumber_xor([4,1,2,1,2])
