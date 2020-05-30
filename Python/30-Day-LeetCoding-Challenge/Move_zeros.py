'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp=0
        n=len(nums)
        for i in range (0,n):
            if nums[i]!=0:
                nums[temp]=nums[i]
                temp=temp+1
                
        while temp<n:
            nums[temp]=0
            temp=temp+1
        return nums
