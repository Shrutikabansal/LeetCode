'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        if l2==None:
            return l1
        temp=ListNode(None)
        
        if l1.val<l2.val:
            temp=l1
            temp.next=self.mergeTwoLists(l1.next,l2)
            
        else:
            temp=l2
            temp.next=self.mergeTwoLists(l1,l2.next)
            
        return temp
