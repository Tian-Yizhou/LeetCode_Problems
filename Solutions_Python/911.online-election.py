'''
Author: Hannah
Date: 2026-10-02 14:03:25
LastEditTime: 2026-10-02 15:18:58
'''
#
# @lc app=leetcode id=911 lang=python3
#
# [911] Online Election
#

# @lc code=start
from collections import defaultdict
import bisect
class TopVotedCandidate:

    # Method: Binary Search
    # time complexity: O(q*logn). q is the query time, n is length of persons
    # space complexity: O(n)

    def __init__(self, persons: list[int], times: list[int]):
        self.times = []
        self.leaders = []
        vote_counts = {}
        max_votes = 0

        for p, t in zip(persons, times):
            # update vote for person p
            vote_counts[p] = vote_counts.get(p, 0) + 1
            # if person p's votes exceed current max
            if vote_counts[p] >= max_votes:
                # update leading candidate
                max_votes = vote_counts[p]
                self.times.append(t)
                self.leaders.append(p)

    def q(self, t: int) -> int:
        # use bisect_right to find first element > t
        idx = bisect.bisect_right(self.times, t) - 1
        # if use one list to store leading candidate, we can do bisect with argument key
        # idx = bisect.bisect_right(self.history, t, key=lambda x: x[0]) - 1
        if idx >= 0:
            return self.leaders[idx]
        else:
            return 0


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end

