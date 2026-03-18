'''
Author: Hannah
Date: 2026-03-18 11:05:27
LastEditTime: 2026-03-18 11:10:34
'''
#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        # when node is not None
        while cur:
            # record the next node of current node
            nxt = cur.next
            # link current node to previous node
            cur.next = pre
            # update previous node to current node
            pre = cur
            # go to next node
            cur = nxt
        
        # return the new head
        return pre
# @lc code=end

