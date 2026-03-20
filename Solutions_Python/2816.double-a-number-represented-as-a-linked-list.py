'''
Author: Hannah
Date: 2026-03-20 15:48:46
LastEditTime: 2026-03-20 16:21:00
'''
#
# @lc app=leetcode id=2816 lang=python3
#
# [2816] Double a Number Represented as a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # function to reverse the link
    def reverse_link(self, l_head):

        pre = None
        cur = l_head
        while cur:
            # record next node
            nxt = cur.next
            # current node link to pre node
            cur.next = pre
            # update pre to cur
            pre = cur
            # update cur to next
            cur = nxt
        
        return pre
    
    # function to calculate the new value of current node
    def node_cal(self, node, carry):

        node_val = node.val if node else 0

        # the total value of doubling and add carry
        total_val = node_val * 2 + carry
        # new value of current node
        carry, new_val = divmod(total_val, 10)

        new_node = ListNode(next=None, val=new_val)
        
        return carry, new_node

        

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = self.reverse_link(head)
        carry = 0

        pre = None
        # double values of reversed link
        while cur or carry != 0:
            
            carry, new_node = self.node_cal(cur, carry)
            # link new_node to pre
            new_node.next = pre
            # update pre node
            pre = new_node
            # if cur is not None, update cur to next
            if cur:
                cur = cur.next

        return pre
# @lc code=end

