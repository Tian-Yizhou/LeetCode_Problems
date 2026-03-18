'''
Author: Hannah
Date: 2026-03-18 00:43:16
LastEditTime: 2026-03-18 01:44:53
'''
#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner:

    def __init__(self):
        self.stack = [(-1, inf)]
        self.cur_day = -1
        

    def next(self, price: int) -> int:
        # if the price of today is greater than a previous day
        # then the price of previous day is not needed
        # because we need to find the first previous day whose price is greater than today's price
        while price >= self.stack[-1][1]:
            self.stack.pop()
        # record date of today
        self.cur_day += 1
        # record price of today
        self.stack.append((self.cur_day, price))

        # the span
        return self.cur_day - self.stack[-2][0]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

