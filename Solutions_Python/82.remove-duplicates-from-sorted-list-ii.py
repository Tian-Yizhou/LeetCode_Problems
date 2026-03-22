'''
Author: Hannah
Date: 2026-03-22 18:28:54
LastEditTime: 2026-03-22 18:52:35
'''
#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head will be deleted if it duplicates, so we need dummy
        dummy = ListNode(next=head)
        cur = dummy
        # when we have next two nodes
        while cur.next and cur.next.next:
            # recode the value of first node
            val = cur.next.val
            # judge whether next node = next next node
            # if the same,
            if val == cur.next.next.val:
                # if next node is not empty, and its value = duplicate value
                while cur.next and cur.next.val == val:
                    # delete the first, link cur to the second
                    cur.next = cur.next.next
                    # note val is fixed, after this loop, all nodes with value val will be deleted
            else:
                # move cur to next node
                cur = cur.next
        
        return dummy.next
# @lc code=end

