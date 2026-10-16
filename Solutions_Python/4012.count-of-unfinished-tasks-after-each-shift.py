'''
Author: Hannah
Date: 2026-10-15 19:35:50
LastEditTime: 2026-10-15 20:05:59
'''
#
# @lc app=leetcode id=4012 lang=python3
#
# [4012] Count of Unfinished Tasks After Each Shift
#

# @lc code=start
import bisect
class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        n = len(tasks)
        # Method 2: Binary Search
        # time complexity: O(N + M*logN), M = len(shifts)
        # space complexity: O(N), N = len(tasks)
        ans = []
        # the prefix sum of tasks
        for i in range(1, n):
            tasks[i] += tasks[i-1]

        # accumulative time we have from shifts
        cum_shift = 0
        for i, shift in enumerate(shifts):
            cum_shift += shift
            # if this shift can complete all tasks remain
            if cum_shift >= tasks[-1]:
                # reset cum_shift for a new start
                cum_shift = 0
                ans.append(0)
            # if this shift cannot complete all tasks, 
            else:
                idx = bisect.bisect_right(tasks, cum_shift)
                # remain tasks start from tasks[idx]
                ans.append(n - idx)

        return ans



        # Method 1: Binary Search, time limit exceed
        # time complexity: O(N)
        # space complexity: O(MN)
        ans = []
        # prefix sum
        pre_s = []
        s = 0
        for num in tasks:
            s += num
            pre_s.append(s)

        cur_pre_s = pre_s
        for num in shifts:
            idx = bisect.bisect_right(cur_pre_s, num)
            # if this shift can complete all tasks, go to next shift
            if idx == n:
                ans.append(0)
                cur_pre_s = pre_s
            # if this shift cannot complete the first task, we have n tasks remian
            elif idx == 0:
                ans.append(n)
                cur_pre_s = [x - num for x in cur_pre_s]
            # the unfinished tasks start from tasks[idx]
            else:
                ans.append(n-idx)
                cur_pre_s = [max(0, x-num) for x in cur_pre_s]

        return ans


# @lc code=end

