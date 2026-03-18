'''
Author: Hannah
Date: 2026-03-18 14:19:01
LastEditTime: 2026-03-18 14:27:13
'''
#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Math: 
        # distance from head to entrance: a
        # distance from entrance to where fast meets slow: b
        # distance from where fast meets slow to entrance: c
        # we have: a = (k-1)(b + c) + c
        # this means when fast meets slow, let head go a steps
        # head will reach the entrance
        # and slow will also reach the entrance
        # so where head meets slow is the entrance

        slow, fast = head, head

        # If there is a cycle (fast will not be None)
        # you will definitely find the entrance
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                while head is not slow:
                    slow = slow.next
                    head = head.next
                return slow

        # If there is not a cycle
        # while loop will be broken    
        return None

# @lc code=end

