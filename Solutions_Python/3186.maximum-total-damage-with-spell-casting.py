'''
Author: Hannah
Date: 2026-03-21 12:24:43
LastEditTime: 2026-03-21 13:55:52
'''
#
# @lc app=leetcode id=3186 lang=python3
#
# [3186] Maximum Total Damage With Spell Casting
#

# @lc code=start
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:

        # Method 3: use an array instead of cache
        cnt = Counter(power)
        spell = sorted(cnt)

        dp = [0] * (len(spell) + 1)

        for i, p in enumerate(spell):
            j = i-1
            while j >= 0 and spell[j] >= p-2:
                j -= 1
            
            # Note: we add 1 more number in dp, so
            # dp[i] means choosing spells from spell[0] to spell[i-1]
            p_no = dp[i]
            # dp[j+1] means choosing spells from spell[0] to spell[j]
            p_yes = dp[j+1] + p * cnt[p]

            dp[i+1] = max(p_no, p_yes)
        
        ans = dp[-1]

        return ans
    
        # Method 2: cache, same logic with method 1
        # record the power and the number of it
        cnt = Counter(power)
        # get the power of spells (keys of cnt, no duplicate)
        spell = sorted(cnt)

        # dp(i): the max damage choosing from spell[0] to spell[i]
        @cache
        def dp(i):
            # boundary: no spell, no damage
            if i < 0:
                return 0
            # the power of spell[i]
            p = spell[i]
            # previous spell
            j = i-1
            # if j hasn't exceed the boundary, 
            # and spell j's power >= p-2
            while j >= 0 and spell[j] >= p-2:
                # move j to previous spell
                j -= 1
            # if we don't use spell[i], the max damage is
            p_no = dp(i-1)
            # if we use spell[i], the max damage is
            p_yes = dp(j) + p * cnt[p]
            # return the max damage until spell[i]
            return max(p_no, p_yes)
        
        return dp(len(spell)-1)


        # Method 1: correct method, but TLE
        n = len(power)
        power.sort()
        ans = 0
        dp = [0]
        for i in range(n):
            # if we don't use power[i], the damage is current max damage
            p_no = ans
            # if we use power[i]
            # count the number of spell whose power is power[i]
            cnt= 1
            # start from previous spell
            j = i-1
            # if j hasn't exceeded the bounded,
            # and it's power[j] >= power[i] - 2
            while j >= 0 and power[j] >= power[i] - 2:
                # if j has the same power with spell i
                if power[j] == power[i]:
                    # add count
                    cnt += 1
                # go to left one
                j -= 1
            # if we use spell i, the max power is calculated as follows
            p_yes = dp[j+1] + power[i] * cnt
            # the max power until i-th spell
            p_i = max(p_no, p_yes)
            dp.append(p_i)
            # update ans
            ans = max(ans, p_i)
        
        return ans


# @lc code=end

