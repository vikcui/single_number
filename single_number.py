# author: YANG CUI
"""
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.
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

def singleNumber_counter(nums):
    """
    Approach: use collections.Counter()
    :param nums: input list of numbers containing only 1 element that appeared once
    :return: that element
    :time complexity: O(n)
    :space complexity: the size of the hash table
    """
    bag = collections.Counter(nums)
    for key in bag.keys():
        if bag[key] == 1:
            return key

# singleNumber_counter([2,2,2,3])

def singleNumber_maths(nums):
    """
    Approach: maths calculations
    Concept: 2 * (a + b + c) - (a + a + b + b + c) = c2∗(a+b+c)−(a+a+b+b+c)=c
    :param nums: input list of numbers containing only 1 element that appeared once
    :return: that element
    :time complexity: O(n)
    :space complexity: O(n)
    """
    return 2 * sum(set(nums)) - sum(nums)

# singleNumber_maths([4,1,2,1,2])