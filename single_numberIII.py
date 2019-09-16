# author: YANG CUI
"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once.
linear time and constant space

idea taken from: https://leetcode.com/problems/single-number-iii/discuss/354583/Python-O(n)-time-O(1)-space-with-examples
"""

def singleNumberIII(nums):
    """
    Approach: bit manipulations (XOR) ^
    Concept: If we take XOR of zero and some bit, it will return that bit. If we take XOR of two same bits, it will return 0
    :param nums: input list of numbers containing only 1 element that appeared once
    :return: that element
    :time complexity: O(n)
    :space complexity: O(1)
    """
    # one pass calculate res1 XOR res2
    res1XORres2 = 0
    for elem in nums:
        res1XORres2 ^= elem
    # find where res1XORres2 is 1, that's the smaller one between the two since we are looping backward
    count = 0
    while count < res1XORres2.bit_length():
        mask = (res1XORres2 >> count) & 1
        if mask == 1:
            break
        count += 1
    # another pass to separate res1 and res2
    res1 = 0
    res2 = 0
    for num in nums:
        if (num >> count) & 1:
            res1 ^= num
        else:
            res2 ^= num
    return [res1, res2]





print(singleNumberIII([1,2,1,3,2,5]))

