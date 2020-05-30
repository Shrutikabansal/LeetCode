'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

class Solution(object):
    def sort_list(self,e):
        return len(e)
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        strs.sort(key=self.sort_list)
        #print(strs)
        n=len(strs)
        if n==0:
            return ""
        flag=0
        m=len(strs[0])
        if m==0:
            return ""
        ans=""
        for i in range (0,m):
            count=0
            for j in range (1,n):
                if strs[0][i]==strs[j][i]:
                    count=count+1
                else:
                    flag=1
                    break
            if flag==1:
                break
            if count==n-1:
                ans=ans+strs[0][i]
                
        return ans
