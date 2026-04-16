from bisect import bisect_left
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        index_map = {}
        for i, val in enumerate(nums):
            index_map.setdefault(val, []).append(i)
        
        result = []
        for q in queries:
            val = nums[q]
            indices = index_map[val]
            
            if len(indices) == 1:
                result.append(-1)
                continue
            
            pos = bisect_left(indices, q)  # indices[pos] == q (always found)
            
            prev_idx = indices[(pos - 1) % len(indices)]
            next_idx = indices[(pos + 1) % len(indices)]
            
            dist1 = min(abs(prev_idx - q), n - abs(prev_idx - q))
            dist2 = min(abs(next_idx - q), n - abs(next_idx - q))
            
            result.append(min(dist1, dist2))
        
        return result