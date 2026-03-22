'''
Author: Hannah
Date: 2026-03-21 18:15:27
LastEditTime: 2026-03-21 19:55:38
'''
#
# @lc app=leetcode id=2944 lang=python3
#
# [2944] Minimum Number of Coins for Fruits
#

# @lc code=start

# from collections import deque
# from functools import cache

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        
        # Method 3: use queue
        n = len(prices)
        # (i, c): buy i-th fruit and the rest fruits, the min coins is c
        # dummy: buy fruit n+1, use 0 coin
        q = deque([(n+1, 0)])

        # backward
        for i in range(n, 0, -1):
            # if fruit q[-1][0] is not in reward range
            while q[-1][0] > i*2 + 1:
                # move it
                q.pop()
            # pay i-th fruit and get the rest with q[-1][1]
            c = prices[i-1] + q[-1][1]
            # if this method cost less, it's currently optimal
            while c <= q[0][1]:
                # we don't need the old method
                q.popleft()
            # add current method to the left
            q.appendleft((i, c))

        return q[0][1]

        # Method 2: use array
        n = len(prices)
        dp = [inf] * n

        for i in range(n-1, -1, -1):
            cur_fruit = i + 1
            if cur_fruit*2 >= n:
                dp[i] = prices[i]
            else:
                dp[i] = prices[i] + min(dp[i+1:2*i+3])
        
        return dp[0]
        
        # Method 1: use cache
        # initialization
        n = len(prices)

        # dp(i): if we buy i-th fruit (pay prices[i-1]),
        #  the min coins to get rest fruits
        @cache
        def dp(i):
            # if i + i >= n
            if i*2 >= n:
                # we just buy i-th fruit and get the rest for free
                return prices[i-1]
            # Otherwise, we need to pay i-th fruit, and
            # we need to find j-th fruit such that
            # the cost is minimum to get rest fruits
            else:
                # the reward range is (i+1)-th fruit to (i+i)-th fruit
                # then from fruit (i+1) to (i+i+1), we must pay at least one fruit
                # So the range of j is [i+1, 2i+1]  
                return prices[i-1] + min(dp(j) for j in range(i+1, 2*i+2))
        
        # we must buy the first fruit
        return dp(1)
        

# @lc code=end

