'''
Author: Hannah
Date: 2026-03-18 11:06:00
LastEditTime: 2026-03-18 12:44:33
'''
#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # get the length of the list
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        
        # compute how many k-list do we need to reverse
        cnt = n // k

        dummy = ListNode(next=head)

        # p0 is the previous node before a new sub-list
        p0 = dummy
        # start from head
        cur = head
        # when we need to do reverse
        while cnt > 0:
            # set an temporary empty node
            pre = None
            # reverse k nodes
            for _ in range(k):
                # record next node
                nxt = cur.next
                # link current node to previous node
                cur.next = pre
                # update pre node to cur node
                pre = cur
                # update cur node to next node
                cur = nxt
            
            # after a k-sublist revision
            # link the first node of k-sublist to the first node next sublist
            p0.next.next = cur
            # record the first node of k-sublist as new p0
            new_p0 = p0.next
            # link p0 to the last node of k-sublist
            p0.next = pre
            # update p0
            p0 = new_p0
            # finish one sublist revision
            cnt -= 1
        
        return dummy.next

# @lc code=end

