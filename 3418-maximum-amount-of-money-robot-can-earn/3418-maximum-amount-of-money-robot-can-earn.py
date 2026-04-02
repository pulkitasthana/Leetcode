from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        # dp[j][k] = max coins at column j with k neutralizations used
        dp = [[float('-inf')] * 3 for _ in range(n)]
        
        # initialize start cell
        v = coins[0][0]
        dp[0][0] = v
        
        if v < 0:
            dp[0][1] = 0   # neutralize first robber
        
        # first row
        for j in range(1, n):
            v = coins[0][j]
            new = [float('-inf')] * 3
            
            for k in range(3):
                if dp[j-1][k] != float('-inf'):
                    # take value normally
                    new[k] = max(new[k], dp[j-1][k] + v)
                    
                    # neutralize if robber
                    if v < 0 and k < 2:
                        new[k+1] = max(new[k+1], dp[j-1][k])
            
            dp[j] = new
        
        # rest of grid
        for i in range(1, m):
            new_row = [[float('-inf')] * 3 for _ in range(n)]
            
            for j in range(n):
                v = coins[i][j]
                
                for k in range(3):
                    # from top
                    if dp[j][k] != float('-inf'):
                        new_row[j][k] = max(new_row[j][k], dp[j][k] + v)
                        
                        if v < 0 and k < 2:
                            new_row[j][k+1] = max(new_row[j][k+1], dp[j][k])
                    
                    # from left
                    if j > 0 and new_row[j-1][k] != float('-inf'):
                        new_row[j][k] = max(new_row[j][k], new_row[j-1][k] + v)
                        
                        if v < 0 and k < 2:
                            new_row[j][k+1] = max(new_row[j][k+1], new_row[j-1][k])
            
            dp = new_row
        
        return max(dp[n-1])