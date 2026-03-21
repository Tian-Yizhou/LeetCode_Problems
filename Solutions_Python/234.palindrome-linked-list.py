'''
Author: Hannah
Date: 2026-03-20 16:26:10
LastEditTime: 2026-03-20 21:00:02
'''
#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # function to find mid
    def find_mid(self, l_head):
        
        slow, fast = l_head, l_head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    # function to reverse link
    def reverse_link(self, l_head):

        pre = None
        cur = l_head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # find the mid node
        mid = self.find_mid(head)
        # reverse the link from mid to end
        head2 = self.reverse_link(mid)

        while head2:
            if head.val == head2.val:
                head = head.next
                head2 = head2.next
            else:
                return False
        
        return True
        
        
# @lc code=end

