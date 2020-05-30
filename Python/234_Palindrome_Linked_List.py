'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack=[]
        
        current=head
        
        while(current!=None):
            stack.append(current.val)
            current=current.next
            
        current=head
        
        while(current!=None):
            if current.val!=stack[-1]:
                return 0
            stack.pop()
            current=current.next
            
        return 1
