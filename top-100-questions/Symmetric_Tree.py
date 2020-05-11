'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mirror(self,r1, r2):
        if r1==None and r2==None:
            return 1
        
        if r1!=None and r2!=None:
            if r1.val==r2.val:
                return self.mirror(r1.left, r2.right) and self.mirror(r1.right,r2.left)
                
                
            else:
                return 0
        else:
            return 0
                
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return 1
        if root.left==None and root.right==None:
            return 1
        return self.mirror(root.left, root.right)
