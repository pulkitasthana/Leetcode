from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        # Expand factory positions based on capacity
        slots = []
        for pos, limit in factory:
            slots.extend([pos] * limit)
        
        m, n = len(robot), len(slots)
        
        # dp[i][j] = min cost to fix first i robots using first j slots
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Base case: 0 robots = 0 cost
        for j in range(n + 1):
            dp[0][j] = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # skip this slot
                dp[i][j] = dp[i][j-1]
                
                # assign robot i-1 to slot j-1
                dp[i][j] = min(
                    dp[i][j],
                    dp[i-1][j-1] + abs(robot[i-1] - slots[j-1])
                )
        
        return dp[m][n]