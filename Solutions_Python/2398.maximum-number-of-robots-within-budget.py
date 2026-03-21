'''
Author: Hannah
Date: 2026-03-21 14:37:13
LastEditTime: 2026-03-21 18:13:45
'''
#
# @lc app=leetcode id=2398 lang=python3
#
# [2398] Maximum Number of Robots Within Budget
#

# @lc code=start
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        ans = 0

        max_q = deque()
        s = 0
        left = 0

        for i, x in enumerate(chargeTimes):
            # add chargeTimes[i] into window, and update max chargeTimes
            while max_q and x >= chargeTimes[max_q[-1]]:
                max_q.pop()
            max_q.append(i)
            
            # update sum
            s += runningCosts[i]

            # make sure under budget after adding i-th robot
            while max_q and chargeTimes[max_q[0]] + (i - left + 1) * s > budget:
                # if over budget, move the left robot
                # update s
                s -= runningCosts[left]
                # move index
                left += 1
                # update max chargeTime if left robot has max chargeTime
                if max_q[0] < left:
                    max_q.popleft()
            # after while loop, current robots <= budget
            # update ans
            ans = max(ans, i-left+1)
        
        return ans
                

# @lc code=end

