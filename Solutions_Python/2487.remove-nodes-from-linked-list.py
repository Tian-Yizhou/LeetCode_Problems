'''
Author: Hannah
Date: 2026-03-22 19:15:51
LastEditTime: 2026-03-22 19:34:06
'''
#
# @lc app=leetcode id=2487 lang=python3
#
# [2487] Remove Nodes From Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # function to reverse the link
    def reverse_link(self, l_node):

        pre = None
        cur = l_node
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre
    
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the link, 
        # then delete any node that has less value than current node
        head = self.reverse_link(head)

        # head is the last node of original link, it wil be preserved in any case
        cur = head
        # if cur has next node
        while cur.next:
            # if next node has less value
            if cur.val > cur.next.val:
                # delete next node
                cur.next = cur.next.next
            # Otherwise, move to next node
            else:
                cur = cur.next
            # after while loop, we get a non-decreasing link
        
        # reverse the non-decreasing link, we get the ans (non-increasing link)
        return self.reverse_link(head)


# @lc code=end

