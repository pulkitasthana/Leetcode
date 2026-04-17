from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # last_seen_reverse maps reverse(nums[i]) -> index i
        last_seen_reverse = {}
        min_dist = float('inf')
        
        for j, val in enumerate(nums):
            # 1. Check if current nums[j] matches reverse(nums[i]) for some i < j
            if val in last_seen_reverse:
                current_dist = j - last_seen_reverse[val]
                if current_dist < min_dist:
                    min_dist = current_dist
            
            # 2. Store reverse(nums[j]) and its index for future j's
            # Using str[::-1] handles the leading zero logic (e.g., "120" -> "021" -> 21)
            rev_val = int(str(val)[::-1])
            last_seen_reverse[rev_val] = j
            
        # If min_dist was never updated, no mirror pair exists
        return min_dist if min_dist != float('inf') else -1