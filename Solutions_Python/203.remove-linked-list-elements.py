'''
Author: Hannah
Date: 2026-03-22 18:53:43
LastEditTime: 2026-03-22 18:57:59
'''
#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # head might be deleted, so we need dummy
        dummy = ListNode(next=head)

        cur = dummy
        # when cur has next node
        while cur.next:
            # if next node has value val
            if cur.next.val == val:
                # delete next node
                cur.next = cur.next.next
            else:
                # cur goes to next node
                cur = cur.next
        
        return dummy.next

# @lc code=end

