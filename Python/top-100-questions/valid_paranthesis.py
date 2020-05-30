'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        n=len(s)
        for i in range (0,n):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            elif s[i]==')' and len(stack)!=0:
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return 0
            elif s[i]=='}' and len(stack)!=0:
                if stack[-1]=='{':
                    stack.pop()
                else:
                    return 0
            elif s[i]==']' and len(stack)!=0:
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return 0
            else:
                return 0
        
        if len(stack)==0:
            return 1
        return 0
