'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        
        
        #temp1=[1]
        #temp2=[1,1]
        #ans.append(temp1)
       # ans.append(temp2)
        
        for i in range (0, n):
            temp=[]
            temp.append(1)
            for j in range (1,i):
                temp.append(ans[i-1][j-1]+ans[i-1][j])
                #print("yui")
            if i!=0:
                temp.append(1)
            ans.append(temp)
            
        return ans
