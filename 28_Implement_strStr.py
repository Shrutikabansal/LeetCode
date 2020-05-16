'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        j = 0
        m = len(needle)
        n = len(haystack)
        if m ==0:
            return 0
        while i<n and n-i+1>=m:
            if haystack[i] == needle[j]:
                temp = i
                while j<m and i<n and needle[j]==haystack[i]:
                    i+=1
                    j+=1
                if j == m:
                    return temp
                i= temp+1
                j = 0
            else:
                  i+=1
        return -1
