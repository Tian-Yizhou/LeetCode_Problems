'''
Author: Hannah
Date: 2026-10-17 11:21:11
LastEditTime: 2026-10-17 13:34:27
'''
#
# @lc app=leetcode id=4008 lang=python3
#
# [4008] Minimum Initial Strength to Defeat All Monsters
#

# @lc code=start
class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:

        # Method 3: Binary Search
        # time complexity: O(B + N + NlogN)
        # space complexity: O(N)
        # find the min strength needed, simulate for each strength
        n = len(monsters)

        # the difference array is bonus now
        bonus = [0] * (n + 1)
        for l, r, v in boosts:
            bonus[l] += v
            # r+1 might be n
            bonus[r + 1] -= v

        for i in range(1, n):
            bonus[i] += bonus[i - 1]

        
        # simulate for a given strength
        def check(strength, monsters, bonus) -> bool:
            for s, b in zip(monsters, bonus):
                if strength + b < s:
                    return False
                strength = max(strength - s, 0)
            return True
        # min strength: 0; max sterngth: sum(monsters)
        left, right = 0, sum(monsters)
        while left <= right:
            mid = (left + right) // 2
            # if current strength is enough, continue search left side
            if check(mid, monsters, bonus):
                right = mid - 1
            else:
                left = mid + 1

        return left

        # Method 2: Greedy, optimize method 1 space complexity
        # time complexity: O(N + B)
        # space complexity: O(N)
        n = len(monsters)
    
        # we only need difference array
        diff = [0] * (n + 1)
        for l, r, v in boosts:
            diff[l] += v
            diff[r + 1] -= v
            
        ans = 0
        current_boost = 0
        current_prefix_sum = 0
        
        # update prefix_sum, current bonus, strength_needed at the same time
        for i in range(n):
            current_boost += diff[i]
            
            # if the bonus is not enough for beat the monster
            if monsters[i] > current_boost:
                # we need `strength_needed` to beat current monster
                strength_needed = monsters[i] - current_boost
                # update answer
                ans = current_prefix_sum + strength_needed
                
            # add this monster's strength into prefix_sum
            current_prefix_sum += monsters[i]
            
        return ans

        # Method 1: Greedy
        # time complexity: O(N + B)
        # space complexity: O(N)
        n = len(monsters)
    
        # get the pre_fix sum of monsters
        # length of prefix_sum is n + 1, 
        # because when i==0, prefix_sum is 0 
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + monsters[i]
            
        # use difference array to construct the strength needed after abstract bonus
        diff = [0] * (n + 1)
        for l, r, v in boosts:
            diff[l] += v
            diff[r + 1] -= v
            
        strength_needed = [0] * n
        current_boost = 0
        for i in range(n):
            current_boost += diff[i]
            strength_needed[i] = max(0, monsters[i] - current_boost)
            
        # find the max index where strength_needed is not zero
        for i in range(n - 1, -1, -1):
            if strength_needed[i] > 0:
                # the answer is all monsters' strength before i plus
                # the strength needed after reducing bonus 
                return prefix_sum[i] + strength_needed[i]
            
        return 0
        
# @lc code=end

