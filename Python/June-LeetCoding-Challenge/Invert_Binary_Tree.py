'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mirror(self, head):
        if head==None:
            return 
        
        self.mirror(head.left)
        self.mirror(head.right)
        
        tmp=head.left
        head.left=head.right
        head.right=tmp
    
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        head=root
        
        self.mirror(head)
        return root
