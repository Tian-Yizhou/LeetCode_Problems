'''
Author: Hannah
Date: 2026-03-22 18:24:39
LastEditTime: 2026-03-22 18:28:40
'''
#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # special case
        if head is None:
            return head
        
        cur = head
        # determine whether cur node only appears once
        while cur.next:
            # if next node has the same value, delete it
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            # when cur is unique, move to next node
            else:
                cur = cur.next
        
        return head
# @lc code=end

