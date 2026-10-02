'''
Author: Hannah
Date: 2026-10-01 18:12:18
LastEditTime: 2026-10-01 19:01:27
'''
#
# @lc app=leetcode id=3508 lang=python3
#
# [3508] Implement Router
#

# @lc code=start
# from collections import defaultdict, deque
# import bisect
class Router:
    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        # the queue to store packet
        self.packet_q = deque()
        # use set to remove duplicate packet
        self.packet_set = set()
        self.dest_to_timestamps = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        # if the packet is already in set, don't add, return False
        if packet in self.packet_set:
            return False
        self.packet_set.add(packet)
        # if current memory limit is achieved
        if len(self.packet_q) == self.memory_limit:
            # remove the earliest packet
            self.forwardPacket()
        # add current packet into queue
        self.packet_q.append(packet)
        self.dest_to_timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        # if current queue is empty
        if not self.packet_q:
            return []
        # FIFO
        packet = self.packet_q.popleft()
        self.packet_set.remove(packet)
        self.dest_to_timestamps[packet[1]].popleft()
        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.dest_to_timestamps[destination]
        left = bisect.bisect_left(timestamps, startTime)  # deque 访问不是 O(1) 的，可以看另一份代码【Python3 list】
        right = bisect.bisect_right(timestamps, endTime)
        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
# @lc code=end

