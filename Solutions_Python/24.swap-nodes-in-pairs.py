'''
Author: Hannah
Date: 2026-03-18 12:45:00
LastEditTime: 2026-03-18 14:02:00
'''
#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # The same method of 25

        # get the length of the list
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        # swap every two nodes
        cnt = n // 2
        dummy = ListNode(next=head)
        p0 = dummy
        cur = head
        while cnt > 0:
            pre = None
            for _ in range(2):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            p0.next.next = cur
            new_p0 = p0.next
            p0.next = pre
            p0 = new_p0
            cnt -= 1
        
        return dummy.next

# @lc code=end

