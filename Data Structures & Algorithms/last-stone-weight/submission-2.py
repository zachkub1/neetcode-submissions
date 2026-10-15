import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, nums: List[int]) -> int:
        heapq.heapify_max(nums)

        while len(nums) > 1:
            x = heapq.heappop_max(nums)
            y = heapq.heappop_max(nums)

            if x != y:
                heapq.heappush_max(nums, x - y)

        return nums[0] if nums else 0