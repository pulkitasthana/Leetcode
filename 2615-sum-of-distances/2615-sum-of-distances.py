from collections import defaultdict
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pos = defaultdict(list)
        
        # Step 1: group indices
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        res = [0] * len(nums)
        
        # Step 2: process each group
        for indices in pos.values():
            n = len(indices)
            
            # prefix sum of indices
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + indices[i]
            
            # compute result for each index
            for i in range(n):
                left = indices[i] * i - prefix[i]
                right = (prefix[n] - prefix[i + 1]) - indices[i] * (n - i - 1)
                res[indices[i]] = left + right
        
        return res