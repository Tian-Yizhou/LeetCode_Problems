#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # function to reverse a link
    def reverse_link(self, l_head):
        
        pre = None
        cur = l_head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre
    
    # function to find the mid node
    def find_mid(self, l_head):

        slow, fast = l_head, l_head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def pairSum(self, head: Optional[ListNode]) -> int:

        ans = 0

        # find the middle node
        mid = self.find_mid(head)
        # reverse the link from mid to end
        head2 = self.reverse_link(mid)

        while head2:
            ans = max(ans, head.val + head2.val)
            head2 = head2.next
            head = head.next
        
        return ans


        
# @lc code=end

