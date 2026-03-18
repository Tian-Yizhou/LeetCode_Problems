'''
Author: Hannah
Date: 2026-03-18 14:06:05
LastEditTime: 2026-03-18 14:09:14
'''
#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow, fast = head, head
        # when fast is the last node or fast is None
        # the slow is answer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
# @lc code=end

