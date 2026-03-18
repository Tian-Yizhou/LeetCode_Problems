#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        # go to the node of left
        p0 = dummy
        for _ in range(left-1):
            p0 = p0.next
        
        # start reversing
        pre = None
        cur = p0.next
        for _ in range(right-left+1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        # now, p0 is node (left-1); pre is node (right); cur is node (right+1)
        # link node (left) to node (right+1)
        p0.next.next = cur
        # link node (left-1) to node (right)
        p0.next = pre

        # head is node 1
        return dummy.next


# @lc code=end

