'''
Author: Hannah
Date: 2026-03-18 14:19:07
LastEditTime: 2026-03-18 15:10:18
'''
#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # a function to find the middle of a list
    def find_mid(self, l):
        slow, fast = l, l
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # a function to reverse a list
    def reverse_list(self, l):
        pre = None
        cur = l
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find the middle node of the whole list
        mid = self.find_mid(head)
        # reverse the right half of list
        head2 = self.reverse_list(mid)

        # when there is still node on the right list
        while head2.next:
            # record next node of both head
            nxt = head.next
            nxt2 = head2.next

            # # link head to head2
            # head.next = head2
            # # link head2 to head.next
            # head2.next = nxt

            # Or, we can link head2 to head.next first
            # then link head to head2
            head2.next = head.next
            head.next = head2
            # update head and head2
            head = nxt
            head2 = nxt2
        

        
# @lc code=end

