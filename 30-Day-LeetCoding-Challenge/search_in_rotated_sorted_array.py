'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution(object):
    def find(self, nums, l, h,target):
        if l>h:
            return -1
        
        m=(l+h)//2
        if nums[m]==target:
               return m
            
        if nums[l]<=nums[m]:
            if target>=nums[l] and target<=nums[m]:
                return(self.find(nums, l,m-1,target))
            else:
                return (self.find(nums, m+1,h,target))
                
        if target>=nums[m] and target<=nums[h]:
            return (self.find(nums, m+1,h,target))
        else:
            return(self.find(nums, l,m-1,target))
            
        return -1
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        l=0
        h=n-1
        
        return self.find(nums,l,h,target)
