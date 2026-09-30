#
# @lc app=leetcode id=1774 lang=python3
#
# [1774] Closest Dessert Cost
#

# @lc code=start
# import bisect
# from math import inf
class Solution:
    def closestCost(self, baseCosts: list[int], toppingCosts: list[int], target: int) -> int:
        # Method 1: DP + biset, 0-1 packing
        # time complexity: O((n+m)V/w), V is max possible price, w = 32 or 64
        # space complexity: O(V)
        # generate all possible prices
        f = 0
        # add base cost
        for b in baseCosts:
            f = f | (1 << b)
        # add topping cost. Duplicate toppingCosts to represent choose twice
        for t in toppingCosts * 2:
            f = f | (f << t)

        # justify whether target can achieve
        if (f >> target) & 1:
            return target
            
        # convert the bitset int to a list, all reachable prices
        valid_prices = []
        temp = f
        i = 0
        while temp > 0:
            if temp & 1:
                valid_prices.append(i)
            temp >>= 1
            i += 1
        # use bisect to find the target
        idx = bisect.bisect_left(valid_prices, target)
        
        ans = inf
        
        # either idx or idx-1 is the answer
        for i in (idx - 1, idx):
            if 0 <= i < len(valid_prices):
                cost = valid_prices[i]
                distance = abs(cost - target)
                diff_ans = abs(ans - target)
                
                # if the distance is closer than old answer, then update answer
                # or the distance is the same but the cost is smaller than target
                if distance < diff_ans or (distance == diff_ans and cost < ans):
                    ans = cost
                    
        return ans



# @lc code=end

