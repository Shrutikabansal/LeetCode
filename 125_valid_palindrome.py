'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return 1
        ans=""
        for i in range (0,len(s)):
            if (s[i]>='A'and s[i]<='Z') or (s[i]>='a' and s[i]<='z') or (s[i]>='0' and s[i]<='9'):
                ans=ans+s[i]
                
        ans=ans.lower()
        
        i=0
        j=len(ans)-1
        
        while i<=j:
            if ans[i]!=ans[j]:
                return 0
            i=i+1
            j=j-1
        return 1
