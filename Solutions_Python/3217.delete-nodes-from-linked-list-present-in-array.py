'''
Author: Hannah
Date: 2026-03-22 18:58:17
LastEditTime: 2026-03-22 19:05:20
'''
#
# @lc app=leetcode id=3217 lang=python3
#
# [3217] Delete Nodes From Linked List Present in Array
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        # head might be deleted, so we need dummy
        dummy = ListNode(next = head)
        cur = dummy
        # if cur has next node
        while cur.next:
            # if next node value is in nums
            if cur.next.val in nums:
                # delete next node
                cur.next = cur.next.next
            # Otherwise, cur go to next node
            else:
                cur = cur.next
        
        return dummy.next
# @lc code=end

