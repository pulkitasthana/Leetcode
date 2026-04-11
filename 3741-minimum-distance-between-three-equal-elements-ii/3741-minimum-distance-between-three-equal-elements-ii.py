from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        
        # Step 1: store indices
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        ans = float('inf')
        
        # Step 2: process each value
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            # sliding window of size 3
            for i in range(len(indices) - 2):
                dist = 2 * (indices[i + 2] - indices[i])
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1