'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''



class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prevsum={}
        n=len(nums)
        for i in range (0,n):
            if nums[i]==0:
                nums[i]=-1
        sum_till=0
        length=0
        for i in range (0,n):
            sum_till=sum_till+nums[i]
            
            if sum_till == 0:
                length=i+1
            if sum_till in prevsum:
                if length < i-prevsum[sum_till]:
                    length= i-prevsum[sum_till]
            else:
                prevsum[sum_till]=i
                
        return length
