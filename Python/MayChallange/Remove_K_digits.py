'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''


class Solution(object):
    def find_first_values(self, char, lis):
        if len(lis)==0:
            lis.append(char)
        else:
            temp=lis[-1]
            
            while temp>char and len(lis)!=0:
                lis.pop()
                if len(lis)!=0:
                    temp=lis[-1]
            lis.append(char)
        
        return 
    
    
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n=len(num)
        if n<=k:
            return "0"
        lis=[]
        
        for i in range (0,k+1):
            self.find_first_values(num[i], lis)
        
        i=i+1
        ans=""
        
        while i<n:
            ans=ans+lis[0]
            #print(ans)
            #print(lis)
            lis.pop(0)
            self.find_first_values(num[i], lis)
            #print(lis)
            i=i+1
            
        ans = ans+lis[0]; 
        lis.pop(0) 
        
        #if len(ans)==0:
        #    return "0"
        
        i=0
        while(ans[i]=='0' and len(ans)!=1):
            ans=ans[1:]

        if len(ans)==0:
            return "0"
            
        return ans
