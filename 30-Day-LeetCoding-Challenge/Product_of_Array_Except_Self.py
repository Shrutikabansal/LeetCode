'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).
'''


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        left=[1 for i in range (n)]
        right=[1 for i in range (n)]
        
        
        for i in range (1,n):
            left[i]=left[i-1]*nums[i-1]
            
        
        for i in range (n-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
            
        for i in range (0,n):
            nums[i]=left[i]*right[i]
        return nums
