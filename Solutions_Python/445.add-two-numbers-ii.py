'''
Author: Hannah
Date: 2026-03-18 12:45:19
LastEditTime: 2026-03-18 13:46:40
'''
#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Method 2: use carry

    # a function to reverse ListNode
    def reverse_list(self, l):
        pre = None
        cur = l
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre
    
    # a function to add two number of the same digit
    def addTwo(self, l1, l2, carry):

        # if l1 is not None, record value; otherwise 0
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0

        # calculation
        carry, l3_val = divmod(l1_val + l2_val + carry, 10)

        # construct node
        l3 = ListNode(val=l3_val)

        return l3, carry


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # reverse ListNode
        l1 = self.reverse_list(l1)
        l2 = self.reverse_list(l2)

        pre = None
        carry = 0
        while l1 or l2 or (carry != 0):
            l3, carry = self.addTwo(l1, l2, carry)
            # if there is any number, update node to new number
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            # link l3 to pre
            l3.next = pre
            # update pre
            pre = l3
        
        return pre


    # Method 1: Data type convertion
    # # convert link to a list of digits
    # def link_to_nums(sefl, l):
    #     cur = l
    #     res = []
    #     while cur:
    #         res.append(str(cur.val))
    #         cur = cur.next
        
    #     return res
    
    # # convert a number to a link by the order of digits
    # def num_to_link(self, num):
        
    #     lst = list(str(num))

    #     lst = [int(x) for x in lst[::-1]]

    #     tmp = None
    #     for x in lst:
    #         node = ListNode(val=x, next=tmp)
    #         tmp = node
        
    #     return tmp


    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     # convert link to a list of digits
    #     l1_nums = self.link_to_nums(l1)
    #     l2_nums = self.link_to_nums(l2)

    #     # concat digits and do calculation
    #     l1_num = int(''.join(l1_nums))
    #     l2_num = int(''.join(l2_nums))
    #     l3_num = l1_num + l2_num

    #     # convert the sum to a link
    #     return self.num_to_link(l3_num)


# @lc code=end

