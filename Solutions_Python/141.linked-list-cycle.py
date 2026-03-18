'''
Author: Hannah
Date: 2026-03-18 14:06:10
LastEditTime: 2026-03-18 14:13:48
'''
#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head

        # If there is a cycle, we will not break while until fast is slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        # if there is not a cycle, while will be broken
        return False
# @lc code=end

