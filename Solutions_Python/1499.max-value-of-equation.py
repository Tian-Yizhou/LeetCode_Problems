'''
Author: Hannah
Date: 2026-03-21 18:15:17
LastEditTime: 2026-03-21 21:49:30
'''
#
# @lc app=leetcode id=1499 lang=python3
#
# [1499] Max Value of Equation
#

# @lc code=start

# from collections import deque

class Solution:

    def equation_value(self, fix_point, change_point):
        term_1 = fix_point[1] + change_point[1]
        term_2 = fix_point[0] - change_point[0]
        return term_1 + term_2

    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:

        # Method 3: Optimization, same logic with method 2
        ans = -inf
        # q records (x_i, y_i-x_i), maintaining decending y_i-x_i
        q = deque()

        for x, y in points:
            # eliminate unfeasible points
            while q and x - q[0][0] > k:
                q.popleft()
            # update ans
            if q:
                ans = max(ans, q[0][1] + x + y)
            # maintaining q in decending y_i-x_i
            while q and y-x >= q[-1][1]:
                q.pop()
            # add current point into q
            q.append((x, y-x))

        return ans
        
        # Method 2: Monotonic queue
        # y_j + y_i + |x_i - x_j| = y_j + x_j + (y_i - x_i)
        # if a new point j is added into feasible set,
        # we just need to calculate y_j + x_j,
        # and pick out the max (y_i - x_i)

        ans = -inf

        # the idx of feasible points (increasing in x)
        q_idx = deque()
        # queue recording (idx, y_i-x_i), descending in y_i-x_i
        q_val = deque()

        for i, point in enumerate(points):
            x, y = point[0], point[1]
            # eliminate unfeasible points
            while q_idx and x - points[q_idx[0][0]][0] > k:
                # if max (y_i-x_i) is not in feasible set, also eliminate it
                if q_val[0][0] <= q_idx.popleft()[0]:
                    q_val.popleft()
            
            # if there exists a feasible point, update ans
            if q_val:
                ans = max(ans, q_val[0][1]+x+y)
            
            # maintain q_val decending
            while q_val and (y-x) >= q_val[-1][1]:
                q_val.pop()
                
            # add point i into queue
            q_idx.append((i, x))
            q_val.append((i, y-x))
        
        return ans

        # Method 1: correct but TLE
        ans = -inf
        q_idx = deque()

        for i, point in enumerate(points):
            # x value of current point
            x = point[0]
            # if q_idx is not empty
            # ensure all x values in q_idx is legal
            while q_idx and x - points[q_idx[0]][0] > k:
                # pop out illegal points
                q_idx.popleft()
            # if there is any legal points in q_idx,
            # calculate equation value, update ans
            if q_idx:
                res = [self.equation_value(point, points[q_idx[j]]) for j in range(len(q_idx))]
                ans = max(ans, max(res))
            # add current point into queue
            q_idx.append(i)
        
        return ans
# @lc code=end

