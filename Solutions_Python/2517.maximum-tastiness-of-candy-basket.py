'''
Author: Hannah
Date: 2026-02-01 11:26:20
LastEditTime: 2026-02-15 00:45:14
'''
#
# @lc app=leetcode id=2517 lang=python3
#
# [2517] Maximum Tastiness of Candy Basket
#

# @lc code=start
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)

        # Method 3
        # we need to change function check because bisect takes a nondecreasing array
        def check(t):
            cnt = 1
            pre = price[0]
            for i in range(1, n):
                if price[i]-pre >= t:
                    cnt += 1
                    pre = price[i]
            
            return False if cnt >= k else True
        
        # the search range of bisect
        search_range = range((price[-1]-price[0]) // (k-1) + 1)
        # find the last False then -1
        # return bisect_right(search_range, False, key=check) - 1
        # or find the first True then -1
        return bisect_left(search_range, True, key=check) - 1

        # check whether we can choose at least k candies if the tastiness is t
        def check(t):
            cnt = 1
            pre = price[0]
            for i in range(1, n):
                if price[i]-pre >= t:
                    cnt += 1
                    pre = price[i]
            
            return True if cnt >= k else False

        # Method 2: open set
        # the range of possible tasiness
        left = 0
        # the min infeasible tasiness is the floor of (price[-1]-price[0])/(k-1)
        right = (price[-1]-price[0]) // (k-1) + 1
        # we want to find the last True
        while left+1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        
        return left
        
        # Method 1
        # the range of possible tasiness
        # the lowest feasible tastiness is 0
        left = 0
        # the max feasible tasiness is the floor of (price[-1]-price[0])/(k-1)
        right = (price[-1]-price[0]) // (k-1)
        # we want to find the last True
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right
        
# @lc code=end

