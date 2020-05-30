'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

size=256
    
class Solution(object):
   
    def equal(self,A,B):
        for i in range (0,size):
            if A[i]!=B[i]:
                return 0
        return 1
    
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        
        n=len(s)
        m=len(p)
        
        ans=[]
        if m>n:
            return ans
        
        count_pattern=[0]*size
        count_window=[0]*size
        
        for i in range (0,m):
            count_pattern[ord(p[i])]+=1
            count_window[ord(s[i])]+=1
            
        for i in range (m,n):
            
            if self.equal(count_pattern,count_window):
                ans.append(i-m)
            count_window[ord(s[i])]+=1
            count_window[ord(s[i-m])]-=1
            
        if self.equal(count_pattern,count_window):
            ans.append(n-m)
                
        return ans
