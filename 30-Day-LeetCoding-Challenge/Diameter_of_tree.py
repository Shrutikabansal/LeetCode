'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findans(self, root, height):
        lh=[0]
        rh=[0]
        ldia=[0]
        rdia=[0]
        
        if root is None:
            height[0]=0
            return 0
        
        ldia[0]=self.findans(root.left, lh)
        rdia[0]=self.findans(root.right, rh)
        height[0]=max(lh[0],rh[0])+1
        
        return (max(lh[0]+rh[0]+1, max(ldia[0], rdia[0])))
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        height=[0]
        height[0]=0
        height[0]=self.findans(root, height)
        if height[0]==0:
            return 0
        else:
            return height[0]-1
        
