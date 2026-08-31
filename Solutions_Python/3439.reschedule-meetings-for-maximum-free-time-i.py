#
# @lc app=leetcode id=3439 lang=python3
#
# [3439] Reschedule Meetings for Maximum Free Time I
#

# @lc code=start
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        # Method 2: optimize space complexity to O(1)
        def get_free(idx):
            if idx == 0:
                return startTime[0]
            if idx == n:
                return eventTime - endTime[-1]
            return startTime[idx] - endTime[idx-1]

        cur_free = 0
        ans = 0
        for i in range(n+1):
            cur_free += get_free(i)
            if i < k:
                continue
            ans = max(ans, cur_free)
            cur_free -= get_free(i-k)

        return ans
        

        # Method 1: merge the k adjasent free time
        # time complexity: O(n)
        # space complexity: O(n)
        free_time = [startTime[0]] + [startTime[i]-endTime[i-1] for i in range(1, n)] + [eventTime - endTime[-1]]
        cur_free = 0
        ans = 0
        for i, free in enumerate(free_time):
            cur_free += free
            # update when i == k, window==k+1
            if i < k:
                continue
            ans = max(ans, cur_free)
            cur_free -= free_time[i-k]

        return ans
                
# @lc code=end

