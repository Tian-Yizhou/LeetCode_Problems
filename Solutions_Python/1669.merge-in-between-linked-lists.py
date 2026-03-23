'''
Author: Hannah
Date: 2026-03-22 19:34:23
LastEditTime: 2026-03-22 19:47:39
'''
#
# @lc app=leetcode id=1669 lang=python3
#
# [1669] Merge In Between Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # a >= 1, so head of list1 will remain
        # the node before a-th node
        pre_a = list1
        for _ in range(a-1):
            pre_a = pre_a.next
        # the node after b-th node
        aft_b = pre_a
        for _ in range(b-a+2):
            aft_b = aft_b.next
        # link pre_a to head of list2
        pre_a.next = list2
        # link the last node of list2 to aft_b
        while list2.next:
            list2 = list2.next
        list2.next = aft_b

        return list1
# @lc code=end

