'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
'''

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        ans=[]
        for i in range (0,N):
            ans.append(0)
            
        n=len(trust)
        
        if n==0:
            return 1
        for i in range (0,n):
            ans[trust[i][1]-1]+=1
        #for i in range (0,N):
         #   print(ans[i]),
        
        value=0

        for i in range (0,N):
            if ans[i]>value:
                value=ans[i]
                index=i+1
          #      print(value, index)
        if value==N-1:
            for i in range (0,n):
                if trust[i][0]==index:
                    return -1
            return index
        return -1
