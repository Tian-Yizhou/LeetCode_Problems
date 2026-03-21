'''
Author: Hannah
Date: 2026-03-18 00:43:22
LastEditTime: 2026-03-20 21:44:22
'''
#
# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse_link(self, l_head):
        pre = None
        cur = l_head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        ans = []

        # Method 2: right to left (reverse link)
        # maintain a stack containing value
        stack_val = []
        
        head_r = self.reverse_link(head)

        while head_r:
            # if stack_val is not empty, 
            # and current value >= stack top
            while stack_val and head_r.val >= stack_val[-1]:
                # then stack top should be substitued
                stack_val.pop()

            # if stack is not empty (current value < stack top)
            if stack_val:
                # we find next greater value for current value
                ans.append(stack_val[-1])
            # if stack is empty
            else:
                # cannot find strictly greater value for current value
                ans.append(0)
                
            # add current value into stack
            stack_val.append(head_r.val)
            # go to next node
            head_r = head_r.next
        
        # because we reversed the link, we need to reverse ans
        return ans[::-1]

        # Method 1: left to right
        # maintain a stack containing index
        # keep the numbers that haven't find the next greater node
        stack_idx = []
        # record value
        stack_val = []

        cur_idx = 0
        while head:
            ans.append(0)
            # if stack is not empty
            while stack_val and head.val > stack_val[-1]:
                ans[stack_idx[-1]] = head.val
                stack_val.pop()
                stack_idx.pop()
            
            # add the index of current node into stack_idx
            stack_idx.append(cur_idx)
            # add the value of current node into stack_val
            stack_val.append(head.val)
            
            # update current idx
            cur_idx += 1
            # go to next node
            head = head.next
        
        return ans

# @lc code=end

