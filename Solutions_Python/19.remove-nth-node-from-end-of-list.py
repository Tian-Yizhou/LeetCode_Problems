'''
Author: Hannah
Date: 2026-03-22 18:16:45
LastEditTime: 2026-03-22 18:24:23
'''
#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy can solve the case when there is only one node
        dummy = ListNode(next=head)
        # set two remarks
        left, right = dummy, dummy
        # move right n steps, then right become the n-th node
        for _ in range(n):
            right = right.next
        # move right to the end, at the same time move left
        while right.next:
            right = right.next
            left = left.next
        # when right achieves the last node, left is the reverse (n-1)-th node
        left.next = left.next.next

        return dummy.next

        
# @lc code=end

