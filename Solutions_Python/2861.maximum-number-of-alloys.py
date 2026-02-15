'''
Author: Hannah
Date: 2026-02-01 11:25:59
LastEditTime: 2026-02-14 22:35:58
'''
#
# @lc app=leetcode id=2861 lang=python3
#
# [2861] Maximum Number of Alloys
#

# @lc code=start
class Solution:

    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        
        m = len(composition)

        # initial value
        alloy = 0

        # Method 1: open interval
        # for each mahcine
        for i in range(m):
            # the composition needed for one alloy using mahcine[i]
            comp = composition[i]

            # assume put all budget in one metal, how many alloys can we make
            max_alloy = min([(budget // cost[j] + stock[j]) // comp[j] for j in range(n)])
            
            # left and lower than left is feasible
            left = 0
            # right and above right is infeasible
            right = max_alloy + 1

            # open interval: (left, right) are not checked
            while left + 1 < right:
                mid = (left + right) // 2
                
                if sum(max(mid * comp[j] - stock[j], 0) * cost[j] for j in range(n)) <= budget:
                    left = mid
                else:
                    right = mid

            # left is the largest feasible number
            alloy = max(alloy, left)
        
        return alloy
    

        # Method 1: close interval
        # for each mahcine
        for i in range(m):
            # the composition needed for one alloy using mahcine[i]
            comp = composition[i]

            # assume put all budget in one metal, how many alloys can we make
            max_alloy = min([(budget // cost[j] + stock[j]) // comp[j] for j in range(n)])
            
            # lowest feasible number is 0
            left = 0
            # highest feasible number is max_alloy
            right = max_alloy

            # close interval: [left, right] are not checked
            while left <= right:
                mid = (left + right) // 2
                
                if sum(max(mid * comp[j] - stock[j], 0) * cost[j] for j in range(n)) <= budget:
                    left = mid + 1
                else:
                    right = mid - 1

            # right is the largest feasible number
            alloy = max(alloy, right)
        
        return alloy


# @lc code=end

