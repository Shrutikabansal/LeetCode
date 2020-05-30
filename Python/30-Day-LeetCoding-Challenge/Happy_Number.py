class Solution(object):

    def findn(self,n):
        ans=0
        while n>0:
            temp=n%10
            ans=ans+pow(temp,2)
            n=n/10
        return ans
            
            
    def isHappy(self, n):
        """ :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        slow=n
        fast=n
        
        while True:
            slow=self.findn(slow)
            fast=self.findn(self.findn(fast))
            if slow!=fast:
                continue
            else:
                break
        return slow==1
                
