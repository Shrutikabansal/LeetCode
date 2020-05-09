'''
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
'''



class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hi =0
        lo = 0
        for i in xrange(len(s)):
            if s[i] == '(':
                lo+=1
                hi+=1
            elif s[i] == ')':
                if lo > 0:
                    lo -=1
                hi -=1
            else:
                if lo > 0:
                    lo-=1
                hi +=1
            if hi < 0:
                return False
  
        return lo == 0
    '''
      stack=[]
        flag=0
        n=len(s)
        count=0
        for i in range (0,n):
            if s[i]=='(':
                stack.append('(')
            elif s[i]=='*':
                if len(stack)!=0:
                    stack.pop()
                else:
                    count=count+1
            if s[i]==')':
                if len(stack)!=0 and stack[-1]=='(':
                    stack.pop()
                elif count>0:
                    count=count-1
                else:
                    flag=1
                    break
            if flag==1:
                break
                
        if flag==1:
            ans=False
        if len(stack)==0:
            ans= True
        elif len(stack)<=count:
            ans= True
        else:
            ans= False
        print(ans)
         '''   
'''            
        stack=[]
        flag=0
        n=len(s)
        count=0
        
        for i in range (0,n):
            if s[i]=='(':
                stack.append('(')
            elif s[i]=='*':
                count=count+1
            if s[i]==')':
                if len(stack)!=0 and stack[-1]=='(':
                    stack.pop()
                elif count>0:
                    count=count-1
                else:
                    flag=1
                    break
            if flag==1:
                break
                
        if flag==1:
            ans1=False
        if len(stack)==0:
            ans1= True
        elif len(stack)<=count:
            ans1= True
        else:
            ans1= False
            
        if ans1==True or ans2== True:
            return True
        return False'''
