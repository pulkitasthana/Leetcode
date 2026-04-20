from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        
        max_dist = 0
        
        # Compare with first house
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                max_dist = j
                break
        
        # Compare with last house
        for i in range(n):
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, n - 1 - i)
                break
        
        return max_dist