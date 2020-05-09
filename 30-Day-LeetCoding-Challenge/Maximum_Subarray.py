class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        s=0
        end=0
        max_so_far=0
        max_end_here=float("-infinity")
        
        n=len(nums)
        
        for i in range (0, n):
            max_so_far+=nums[i]
            
            if max_so_far>max_end_here:
                max_end_here=max_so_far
                end=i
                start=s
                
            
            if max_so_far<0:
                max_so_far=0
                s=i+1
                
        
        return max_end_here
